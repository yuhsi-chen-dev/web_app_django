from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def profile_view(request: HttpRequest) -> HttpResponse:
    profile = request.user.profile
    return render(request, "users/profile.html", {"profile": profile})


def profile_edit_view(request: HttpRequest) -> HttpResponse:
    return render(request, "users/profile_edit.html")
