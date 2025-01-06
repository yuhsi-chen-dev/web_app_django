import requests
from bs4 import BeautifulSoup
from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from posts.core import PostCreateForm

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
    Render the post creation page and handle form submissions.

    This view displays a form for creating a new post. If the form is submitted
    via POST, it validates the input, extracts additional data from the provided
    URL using BeautifulSoup, and saves the post to the database.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse:
            - A rendered HTML response for the post creation page (GET request).
            - A redirect to the home page upon successful post creation (POST request).

    Key Operations:
        - Fetch metadata (image, title, artist) from the provided URL.
        - Save the data to the `Post` model.

    Dependencies:
        - requests: Fetch external web page content.
        - BeautifulSoup: Parse HTML to extract specific data.
    """
    form = PostCreateForm()

    if request.method == "POST":
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)

            website = requests.get(form.data["url"])
            sourcecode = BeautifulSoup(website.text, "html.parser")

            find_image = sourcecode.select(
                'meta[content^="https://live.staticflickr.com/"]'
            )
            image = find_image[0]["content"]
            post.image = image

            find_title = sourcecode.select("h1.photo-title")
            title = find_title[0].text.strip()
            post.title = title

            find_artist = sourcecode.select("a.owner-name")
            artist = find_artist[0].text.strip()
            post.artist = artist

            post.save()
            return redirect("home")

    return render(request, "posts/post_create.html", {"form": form})


def post_delete_view(request: HttpRequest, pk: int) -> HttpResponse:
    post = Post.objects.get(id=pk)

    if request.method == "POST":
        post.delete()
        messages.success(request, "Post deleted")
        return redirect("home")

    return render(request, "posts/post_delete.html", {"post": post})
