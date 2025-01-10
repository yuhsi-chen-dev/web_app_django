from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404

from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Signal receiver to handle Profile creation and update when a User is saved.

    Args:
        sender (type): The model class (User) that sent the signal.
        instance (User): The User instance being saved.
        created (bool): A boolean indicating whether this is a new User instance.
        **kwargs: Additional keyword arguments provided by the signal.

    Side Effects:
        - Creates a new Profile instance if the User is newly created.
        - Updates the Profile's email field if the User already exists.
    """
    user = instance
    if created:
        Profile.objects.create(user=user, email=user.email)
    else:
        profile = get_object_or_404(Profile, user=user)
        profile.email = user.email
        profile.save()


@receiver(post_save, sender=Profile)
def update_user(sender, instance, created, **kwargs):
    """
    Signal receiver to handle User email updates when a Profile is saved.

    Args:
        sender (type): The model class (Profile) that sent the signal.
        instance (Profile): The Profile instance being saved.
        created (bool): A boolean indicating whether this is a new Profile instance.
        **kwargs: Additional keyword arguments provided by the signal.

    Side Effects:
        - Updates the associated User's email field if it differs from the Profile's email.
    """
    profile = instance
    if created == False:
        user = get_object_or_404(User, id=profile.user.id)
        if user.email != profile.email:
            user.email = profile.email
            user.save()
