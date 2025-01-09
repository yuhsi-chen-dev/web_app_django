from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def profile_view(request: HttpRequest) -> HttpResponse:
    return render(request, "users/profile.html")
