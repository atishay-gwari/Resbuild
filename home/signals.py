from django.db.models.signals import post_save,post_delete
from .models import *
from django.dispatch import receiver
import sys
print(sys.setrecursionlimit(1500))

@receiver(post_save, sender=Project)
def link_project_to_user(sender, instance, created, **kwargs):
    import inspect
    for frame_record in inspect.stack():
        if frame_record[3]=='get_response':
            request = frame_record[0].f_locals['request']
            break
    else:
        request = None
    if created:
        data=Project.objects.get(id=instance.id)
        data.user_name=request.user
        data.save()

    elif not created:
        data=Project.objects.filter(id=instance.id).update(user_name=request.user)
        


@receiver(post_save, sender=Profile)
def link_profile_to_user(sender, instance, created, **kwargs):
    import inspect
    for frame_record in inspect.stack():
        if frame_record[3]=='get_response':
            request = frame_record[0].f_locals['request']
            break
    else:
        request = None
    if created:
        data=Profile.objects.get(id=instance.id)
        data.user_name=request.user
        data.save()

    elif not created:
        data=Profile.objects.filter(id=instance.id).update(user_name=request.user)


@receiver(post_save, sender=Education)
def link_education_to_user(sender, instance, created, **kwargs):
    import inspect
    for frame_record in inspect.stack():
        if frame_record[3]=='get_response':
            request = frame_record[0].f_locals['request']
            break
    else:
        request = None
    if created:
        data=Education.objects.get(id=instance.id)
        data.user_name=request.user
        data.save()

    elif not created:
        data=Education.objects.filter(id=instance.id).update(user_name=request.user)



@receiver(post_save, sender=WorkExp)
def link_workexp_to_user(sender, instance, created, **kwargs):
    import inspect
    for frame_record in inspect.stack():
        if frame_record[3]=='get_response':
            request = frame_record[0].f_locals['request']
            break
    else:
        request = None
    if created:
        data=WorkExp.objects.get(id=instance.id)
        data.user_name=request.user
        data.save()

    elif not created:
        data=WorkExp.objects.filter(id=instance.id).update(user_name=request.user)


@receiver(post_save, sender=SpecialSkill)
def link_skill_to_user(sender, instance, created, **kwargs):
    import inspect
    for frame_record in inspect.stack():
        if frame_record[3]=='get_response':
            request = frame_record[0].f_locals['request']
            break
    else:
        request = None
    if created:
        data=SpecialSkill.objects.get(id=instance.id)
        data.user_name=request.user
        data.save()

    elif not created:
        data=SpecialSkill.objects.filter(id=instance.id).update(user_name=request.user)