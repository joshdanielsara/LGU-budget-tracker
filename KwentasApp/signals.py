# KwentasApp/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, UserProfile

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    """Create a UserProfile for each new CustomUser instance."""
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    """Save the UserProfile instance whenever the CustomUser instance is saved."""
    if hasattr(instance, 'userprofile'):
        instance.userprofile.save()
