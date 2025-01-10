from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from users.core import ProfileForm


def profile_view(request: HttpRequest) -> HttpResponse:
    profile = request.user.profile
    return render(request, "users/profile.html", {"profile": profile})


def profile_edit_view(request: HttpRequest) -> HttpResponse:
    form = ProfileForm(instance=request.user.profile)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect("profile")

    return render(request, "users/profile_edit.html", {"form": form})
