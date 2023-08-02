from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from WiredWorldProject import settings
from WiredWorldProject.account.models import Profile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def create_profile(instance, created, *args, **kwargs):
    if created:
        profile = Profile(email=instance.email, client=instance)
        profile.save()

        html_message = render_to_string('emails/registration.html', {'user': instance})
        plain_message = strip_tags(html_message)
        send_mail(
            subject='Welcome to Wired World',
            message=plain_message,
            html_message=html_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[instance.email]
        )
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


