from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """
    Represents a user profile, extending the default User model with additional fields.

    Attributes:
        user (User): A one-to-one relationship with the built-in User model, ensuring each user has one profile.
        image (ImageField): An optional profile image, stored in the 'avatars/' directory.
        realname (str): An optional field for the user's real name, limited to 20 characters.
        email (str): A unique and optional email address for the profile.
        location (str): An optional field for the user's location, limited to 20 characters.
        bio (str): An optional field for the user's biography.
        created (datetime): The timestamp indicating when the profile was created, automatically set at creation.

    Methods:
        __str__():
            Returns a string representation of the profile, using the associated user's username.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="avatarts/", null=True, blank=True)
    realname = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(unique=True, null=True)
    location = models.CharField(max_length=20, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)
