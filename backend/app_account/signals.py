from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import User


@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    """
    send a welcome email when a user is created
    """
    print("***** Signal for sending welcome email is triggered *****")
    if created:
        send_mail(
            "Welcome!",
            "Thanks for signing up",
            "admin@gmail.com",
            [instance.email],
            fail_silently=False,
        )
