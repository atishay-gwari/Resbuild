from cgitb import text
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import EducationForm, ProfileForm, ProjectForm, SkillForm, WorkexpForm
from .models import *
from django.contrib.auth import login,logout,authenticate,get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required,permission_required
# Create your views here.
from django.views.decorators.cache import never_cache
from django.http  import HttpResponse 
from django.template.loader import get_template
from xhtml2pdf import pisa

@login_required(login_url='login')
def convert(request):
    profiledata=Profile.objects.filter(user_name=request.user)
    edudata=Education.objects.filter(user_name=request.user)
    workdata=WorkExp.objects.filter(user_name=request.user)
    projdata=Project.objects.filter(user_name=request.user)
    skilldata=SpecialSkill.objects.filter(user_name=request.user)
    context={"profiledata":profiledata,"edudata":edudata,"workdata":workdata,"projdata":projdata,"skilldata":skilldata}
    return render(request,'converter.html',context)
    # return FileResponse(buf,as_attachment=True,filename="resume.pdf")

@login_required(login_url='login')
def pdfconvert(request):
    
    profiledata=Profile.objects.filter(user_name=request.user)
    edudata=Education.objects.filter(user_name=request.user)
    workdata=WorkExp.objects.filter(user_name=request.user)
    projdata=Project.objects.filter(user_name=request.user)
    skilldata=SpecialSkill.objects.filter(user_name=request.user)
    template_path = 'conpdf.html'
    context={"profiledata":profiledata,"edudata":edudata,"workdata":workdata,"projdata":projdata,"skilldata":skilldata}
    
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def home(request):
    return render(request,'index.html')


def contactus(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('email') and request.POST.get('msg'):
            post=Contact()
            post.name= request.POST.get('name')
            post.email= request.POST.get('email')
            post.msg= request.POST.get('msg')
            post.save()
                
            return render(request, 'index.html')  

    else:
        return render(request,'contacts.html')

@login_required(login_url='login')
def viewResume(request):
    
    try:
        profiledata=Profile.objects.filter(user_name=request.user)
        edudata=Education.objects.filter(user_name=request.user)
        workdata=WorkExp.objects.filter(user_name=request.user)
        projdata=Project.objects.filter(user_name=request.user)
        skilldata=SpecialSkill.objects.filter(user_name=request.user)
        context={"profiledata":profiledata,"edudata":edudata,"workdata":workdata,"projdata":projdata,"skilldata":skilldata}
    except:
        context={"profiledata":"None","edudata":"None","workdata":"None","projdata":"None","skilldata":"None"}
    return render(request,'ViewResume.html',context)



def signuppage(request):
    if request.method == 'POST':
        user=request.POST['Name']
        e_mail=request.POST['email']
        password1=request.POST['password']
        confirmpassword=request.POST['confirmpassword']

        if password1==confirmpassword:
            if not User.objects.filter(username=user).exists():
        
                if not User.objects.filter(email=e_mail).exists():
            
                    user=User.objects.create_user(username = user, email = e_mail, password=password1)
                    user.save()
            
        return redirect('login')
    return render(request,'signup.html')


def loginpage(request):
    if request.method=='POST':
        username=request.POST['Name']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            # print(user)
            login(request,user)
            return redirect('home')
        # print(email,password)
        else:
            # print("Error 404: credentials doesnt exist")
            return redirect('login')
    else:
        return render(request,'login.html')

from django.views.decorators.cache import cache_control

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='login')
def logoutpage(request):
    # print("logout")
    logout(request)
    return redirect('home')



##################################################################################
# Profile DB
 


@login_required(login_url='login')
def deleteProfile(request,id):
    data=Profile.objects.get(id=id)
    # messages.warning(request,'Project Deleted Successfully')
    data.delete()
    return redirect('view')


@login_required(login_url='login')
# @permission_required('home.add_profile',login_url='home')
def addProfile(request):
    form=ProfileForm()
    # form1=UserCreationForm()
    if request.method == 'POST':
        myData=ProfileForm(request.POST)
        if myData.is_valid():
            myData.save()
            return redirect('view')
    context={"form":form}
    return render(request,'addProfile.html',context)


@login_required(login_url='login')
# @permission_required('home.change_profile',login_url='home')
def updateProfile(request,id):
    data=Profile.objects.get(id=id)
    updateform=ProfileForm(request.POST or None,instance=data)
    if updateform.is_valid():
        updateform.save()
        return redirect('view')
    context={"form":updateform}
    return render(request,'updateProfile.html',context)

##############################################################################
# Education DB

@login_required(login_url='login')
# @permission_required('home.delete_profile',login_url='home')
def deleteEDU(request,id):
    data=Education.objects.get(id=id)
    # messages.warning(request,'Project Deleted Successfully')
    data.delete()
    return redirect('view')


@login_required(login_url='login')
# @permission_required('home.add_profile',login_url='home')
def addEDU(request):
    form=EducationForm()
    if request.method == 'POST':
        # print("yugay")
        myData=EducationForm(request.POST)
        if myData.is_valid():
            myData.save()
            # messages.success(request,'Project Added Successfully')
            return redirect('view')
    context={"form":form}
    return render(request,'addEducation.html',context)

@login_required(login_url='login')
# @permission_required('home.change_profile',login_url='home')
def updateEDU(request,id):
    data=Education.objects.get(id=id)
    updateform=EducationForm(request.POST or None,instance=data)
    if updateform.is_valid():
        updateform.save()
        return redirect('view')
    context={"form":updateform}
    return render(request,'updateEducation.html',context)


################################################################
#WORK EXP DB
@login_required(login_url='login')
# @permission_required('home.delete_profile',login_url='home')
def deleteWORK(request,id):
    data=WorkExp.objects.get(id=id)
    # messages.warning(request,'Project Deleted Successfully')
    data.delete()
    return redirect('view')


@login_required(login_url='login')
# @permission_required('home.add_profile',login_url='home')
def addWORK(request):
    form=WorkexpForm()
    if request.method == 'POST':
        myData=WorkexpForm(request.POST)
        if myData.is_valid():
            myData.save()
            # messages.success(request,'Project Added Successfully')
            return redirect('view')
    context={"form":form}
    return render(request,'addWork.html',context)

@login_required(login_url='login')
# @permission_required('home.change_profile',login_url='home')
def updateWORK(request,id):
    data=WorkExp.objects.get(id=id)
    updateform=WorkexpForm(request.POST or None,instance=data)
    if updateform.is_valid():
        updateform.save()
        return redirect('view')
    context={"form":updateform}
    return render(request,'updateWork.html',context)

###############################################################################################################
#PROJECT DB

@login_required(login_url='login')
# @permission_required('home.delete_profile',login_url='home')
def deletePROJ(request,id):
    data=Project.objects.filter(id=id)
    # messages.warning(request,'Project Deleted Successfully')
    data.delete()
    return redirect('view')


@login_required(login_url='login')
# @permission_required('home.add_profile',login_url='home')
def addPROJ(request):
    form=ProjectForm()
    if request.method == 'POST':
        myData=ProjectForm(request.POST)
        if myData.is_valid():
            myData.save()
            # messages.success(request,'Project Added Successfully')
            return redirect('view')
    context={"form":form}
    return render(request,'addProject.html',context)

@login_required(login_url='login')
# @permission_required('home.change_profile',login_url='home')
def updatePROJ(request,id):
    data=Project.objects.get(id=id)
    updateform=ProjectForm(request.POST or None,instance=data)
    if updateform.is_valid():
        updateform.save()
        return redirect('view')
    context={"form":updateform}
    return render(request,'updateProject.html',context)


#################################################################################################
#Special SKill DB

@login_required(login_url='login')
# @permission_required('home.delete_profile',login_url='home')
def deleteSPECIAL(request,id):
    data=SpecialSkill.objects.get(id=id)
    # messages.warning(request,'Project Deleted Successfully')
    data.delete()
    return redirect('view')


@login_required(login_url='login')
# @permission_required('home.add_profile',login_url='home')
def addSPECIAL(request):
    form=SkillForm()
    if request.method == 'POST':
        myData=SkillForm(request.POST)
        if myData.is_valid():
            myData.save()
            # messages.success(request,'Project Added Successfully')
            return redirect('view')
    context={"form":form}
    return render(request,'addSkill.html',context)

@login_required(login_url='login')
# @permission_required('home.change_profile',login_url='home')
def updateSPECIAL(request,id):
    data=SpecialSkill.objects.get(id=id)
    updateform=SkillForm(request.POST or None,instance=data)
    if updateform.is_valid():
        updateform.save()
        return redirect('view')
    context={"form":updateform}
    return render(request,'updateSkill.html',context)

# #########################################################################################################