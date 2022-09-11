from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import ProfileForm
from .models import Profile,Contact
from django.contrib.auth import login,logout,authenticate,get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required,permission_required
# Create your views here.
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
@permission_required('home.delete_profile',login_url='home')
def deleteResume(request,id):
    data=Profile.objects.get(id=id)
    # messages.warning(request,'Project Deleted Successfully')
    data.delete()
    return redirect('view')

@login_required(login_url='login')
@permission_required('home.change_profile',login_url='home')
def updateResume(request,id):
    data=Profile.objects.get(id=id)
    updateform=ProfileForm(request.POST or None,instance=data)
    if updateform.is_valid():
        updateform.save()
        return redirect('view')
    context={"form":updateform}
    return render(request,'updateResume.html',context)

@login_required(login_url='login')
def viewResume(request):
    
    try:
        data=Profile.objects.all()
        context={"data":data}
    except:
        context={"data":"No data Found"}
    return render(request,'ViewResume.html',context)

@login_required(login_url='login')
@permission_required('home.add_profile',login_url='home')
def addResume(request):
    form=ProfileForm()
    if request.method == 'POST':
        myData=ProfileForm(request.POST)
        if myData.is_valid():
            myData.save()
            messages.success(request,'Project Added Successfully')
            return redirect('home')
    context={"form":form}
    return render(request,'addResume.html',context)

@login_required(login_url='login')
def convert(request):
    return render(request,'converter.html')

def signuppage(request):
    if request.method == 'POST':
        username=request.POST['Name'],
        email=request.POST['email'],
        first_name=request.POST['firstname'],
        last_name=request.POST['lastname']
        password=request.POST['password']
        # confirm_password=request.POST['confirm_password']
        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
            
                new_user=User(username=username, email=email,first_name=first_name,last_name=last_name)

                new_user.set_password(password)
                # new_user.set_confirm_password(confirm_password)
                new_user.save()
            
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
            print("Error 404: credentials doesnt exist")
            return redirect('signup')
    return render(request,'login.html')

def logoutpage(request):
    # print("logout")
    logout(request)
    return redirect('home')
    