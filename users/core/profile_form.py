from django import forms
from django.forms import ModelForm

from ..models import *


class ProfileForm(ModelForm):
    """
    A form for editing the user's profile.

    This form is based on the Profile model and excludes the "user" field.
    It includes customized labels and widgets for specific fields.

    Attributes:
        Meta:
            model (Profile): The model associated with this form.
            exclude (list): A list of fields to exclude from the form.
            labels (dict): Custom labels for fields.
            widgets (dict): Custom widgets for fields, e.g., file input and text area.
    """

    class Meta:
        model = Profile
        exclude = ["user"]
        labels = {
            "realname": "Name",
        }
        widgets = {"image": forms.FileInput(), "bio": forms.Textarea(attrs={"rows": 3})}
