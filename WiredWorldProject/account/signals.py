from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from WiredWorldProject.account.models import Profile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def create_profile(instance, created, *args, **kwargs):
    if created:
        profile = Profile(email=instance.email, client=instance)
        profile.save()
    else:
        profile = Profile.objects.get(client=instance)
        if profile.email != instance.email:
            profile.email = instance.email
            profile.save()


@receiver(post_save, sender=Profile)
def change_client_email(instance, *args, **kwargs):
    client = instance.client
    profile = instance
    if client.email != profile.email:
        client.email = profile.email
        client.save()


