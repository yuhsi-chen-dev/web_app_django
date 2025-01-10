from django.contrib.auth.models import User
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from users.core import ProfileForm


def profile_view(request: HttpRequest, username=None) -> HttpResponse:
    """
    Display the profile page of a specific user, either the currently logged-in user or a user identified by `username`.

    Args:
        request (HttpRequest): The HTTP request object containing user session data, including the logged-in user.
        username (str, optional): The username of a specific user whose profile is to be displayed. If not provided,
            the profile of the currently logged-in user will be shown.

    Returns:
        HttpResponse: A rendered HTML response containing the profile page template, populated with the user's profile data.

    Raises:
        Http404: If the profile of the specified user cannot be found.
    """
    if username:
        profile = get_object_or_404(User, username=username).profile
    else:
        try:
            profile = request.user.profile
        except:
            raise Http404("User not found")
    return render(request, "users/profile.html", {"profile": profile})


def profile_edit_view(request: HttpRequest) -> HttpResponse:
    """
    Handle the profile edit functionality for the currently logged-in user.

    Args:
        request (HttpRequest): The HTTP request object containing user session data
                               and potential form data for profile editing.

    Returns:
        HttpResponse: The rendered profile edit page template with the form or a redirect
                      to the profile page upon successful form submission.
    """
    form = ProfileForm(instance=request.user.profile)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect("profile")

    return render(request, "users/profile_edit.html", {"form": form})
