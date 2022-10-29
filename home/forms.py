from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        # fields="__all__"
        fields=['name','address','phoneno','email','github','linkedin']


class SkillForm(forms.ModelForm):
    class Meta:
        model=SpecialSkill
        # fields="__all__"
        fields=['skill']

class EducationForm(forms.ModelForm):
    class Meta:
        model=Education
        # fields="__all__"
        fields=['university','degree','stream','currentYear','univStartingYear','univPassingYear','univResult']

class WorkexpForm(forms.ModelForm):
    class Meta:
        model=WorkExp
        # fields="__all__"
        fields=['jobTitle','jobStartDate','jobEndDate','jobDescription']

class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        # fields="__all__"
        fields=['projectTitle','projectDescription','projectStartDate','projectEndDate','techStack']