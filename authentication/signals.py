from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import Profile
@receiver(post_save,sender = get_user_model())
def create_new_profile(sender,instance,created,**kwargs):
    print('create_new_profile is called')
    if created:
        new_profile = Profile.objects.create(user=instance)
        print(f'Created profile for {instance.username}')


