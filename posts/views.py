from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import *


def home_view(request: HttpRequest) -> HttpResponse:
    """
    Render the home page with a list of all posts.

    This view queries all `Post` objects from the database and passes them
    to the `home.html` template for rendering. The template can then display
    the list of posts dynamically.

    Args:
        request (HttpRequest): The HTTP request object containing metadata about the request.

    Returns:
        HttpResponse: A rendered HTML response containing the list of posts.
    """
    posts = Post.objects.all()
    return render(request, "posts/home.html", {"posts": posts})


def post_create_view(request: HttpRequest) -> HttpResponse:
    """
    Render the post creation page.

    This view simply renders the `post_create.html` template for creating a new post.

    Args:
        request (HttpRequest): The HTTP request object containing metadata about the request.

    Returns:
        HttpResponse: A rendered HTML response for the post creation page.
    """
    return render(
        request,
        "posts/post_create.html",
    )
