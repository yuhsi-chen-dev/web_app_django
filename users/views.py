from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from users.core import ProfileForm


def profile_view(request: HttpRequest) -> HttpResponse:
    """
    Display the profile page of the currently logged-in user.

    Args:
        request (HttpRequest): The HTTP request object containing user session data.

    Returns:
        HttpResponse: The rendered profile page template with the user's profile data.
    """
    profile = request.user.profile
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
