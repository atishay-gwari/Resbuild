from django.db import models
from django.contrib.auth.models import User
#tables: job,education,personalinfo
# Create your models here.
class Profile(models.Model):
    # userid = models.CharField(max_length=50)
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=100)
    # objective = models.CharField(max_length=500,blank=True,null=True)
    address = models.CharField(max_length=200)
    phoneno = models.CharField(max_length=12)
    email = models.EmailField(max_length=100)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    def __str__(self):
        return f"{self.user_name},{self.name},{self.email}"
    class Meta:
        verbose_name_plural ="Profile"

class Education(models.Model):
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    university = models.CharField(max_length=100, blank=True)
    degree= models.CharField(max_length=50, blank=True)
    stream = models.CharField(max_length=100, blank=True)
    currentYear = models.CharField(max_length=50, blank=True)
    univStartingYear = models.CharField(max_length=20, blank=True)
    univPassingYear = models.CharField(max_length=20, blank=True)
    univResult = models.CharField(max_length=20, blank=True)
    def __str__(self):
        return f"{self.user_name},{self.university},{self.currentYear}"
    class Meta:
        verbose_name_plural ="Education"



class WorkExp(models.Model):
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    jobTitle = models.CharField(max_length=100, blank=True)
    jobStartDate = models.CharField(max_length=20, blank=True)
    jobEndDate = models.CharField(max_length=20, blank=True)
    jobDescription = models.CharField(max_length=500,blank=True,null=True)
    def __str__(self):
        return f"{self.user_name},{self.jobTitle}"
    class Meta:
        verbose_name_plural ="WorkExp"


class Project(models.Model):
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    projectTitle = models.CharField(max_length=100, blank=True)
    projectStartDate = models.CharField(max_length=20, blank=True)
    projectEndDate = models.CharField(max_length=20, blank=True)
    projectDescription = models.CharField(max_length=500,blank=True,null=True)
    techStack = models.CharField(max_length=100, blank=True,null=True)
    def __str__(self):
        return f"{self.user_name},{self.projectTitle}"
    class Meta:
        verbose_name_plural ="Projects"



class SpecialSkill(models.Model):
    user_name=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    skill=models.CharField(max_length=100,null=True,blank=True)
    # description=models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return f"{self.user_name},{self.skill}"
    class Meta:#to remove s in table name in admin page of django app
        verbose_name_plural = "Special Skills"
class Contact(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(blank=True,null=True)
    # phoneno = models.CharField(max_length=12)
    msg = models.CharField(max_length=500,blank=True,null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Contact Us"
    