from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginpage,name="login"),
    path('logout/',views.logoutpage,name='logout'),
    path('signup/', views.signuppage,name="signup"),
    path('', views.home,name="home"),
    path('contact/', views.contactus,name="contactus"),
    path('converter/', views.convert,name="converter"),

    path('addResume/', views.addResume,name="addResume"),
    path('viewResume/', views.viewResume,name="view"),
    path('delete/<str:id>/', views.deleteResume,name="delete"),
    path('update/<str:id>/', views.updateResume,name="update")



]
