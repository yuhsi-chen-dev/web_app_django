from django import forms
from django.forms import ModelForm

from ..models import *


class PostCreateForm(ModelForm):
    """
    A form class for creating new posts.

    This form is bound to the `Post` model and allows users to input data
    for all fields in the model. It includes custom labels and widget configurations
    for enhanced usability.

    Attributes:
        Meta: Defines metadata for the form, including the model it is bound to,
        the fields to include, custom labels, and widget configurations.
    """

    class Meta:
        model = Post
        fields = "__all__"
        labels = {
            "body": "Caption",
        }
        widgets = {
            "body": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Add a caption ...",
                    "class": "font1 text-4xl",
                }
            ),
        }
