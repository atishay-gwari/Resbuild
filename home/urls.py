from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.loginpage,name="login"),
    path('logout/',views.logoutpage,name='logout'),
    path('signup/', views.signuppage,name="signup"),
    path('', views.home,name="home"),
    path('contact/', views.contactus,name="contactus"),
    path('converter/', views.convert,name="converter"),
    path('download/pdf/', views.pdfconvert,name="pdfcon"),
    path('viewResume/', views.viewResume,name="view"),
    path('addProfle/', views.addProfile,name="addprofile"),
    path('delete/<str:id>/', views.deleteProfile,name="delete"),
    path('update/<str:id>/', views.updateProfile,name="update"),


    path('add/EDU/', views.addEDU,name="addeDU"),
    path('delete/EDU/<str:id>/', views.deleteEDU,name="deleteEDU"),
    path('update/EDU/<str:id>/', views.updateEDU,name="updateEDU"),


    path('add/work/', views.addWORK,name="addWork"),
    path('delete/work/<str:id>/', views.deleteWORK,name="deleteWork"),
    path('update/work/<str:id>/', views.updateWORK,name="updateWork"),

    path('add/proj/', views.addPROJ,name="addproj"),
    path('delete/proj/<str:id>/', views.deletePROJ,name="deleteproj"),
    path('update/proj/<str:id>/', views.updatePROJ,name="updateproj"),

    path('add/skill/', views.addSPECIAL,name="addskill"),
    path('delete/skill/<str:id>/', views.deleteSPECIAL,name="deleteskill"),
    path('update/skill/<str:id>/', views.updateSPECIAL,name="updateskill"),

    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="password_rest.html"),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),name="password_reset_confirm"),
    path('reset_password_done/',auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),name="password_reset_complete"),
    # path('accounts/',)
]
