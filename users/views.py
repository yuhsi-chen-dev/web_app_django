from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from posts.core import ReplyCreateForm
from users.core import ProfileForm


def profile_view(request: HttpRequest, username=None) -> HttpResponse:
    """
    Display the profile page of a specific user, either the currently logged-in user or a user identified by `username`.

    Args:
        request (HttpRequest): The HTTP request object containing user session data, including the logged-in user.
        username (str, optional): The username of a specific user whose profile is to be displayed. If not provided,
            the profile of the currently logged-in user will be shown.

    Returns:
        HttpResponse: A rendered HTML response containing the profile page template, populated with the user's profile data
                      and the user's posts. If the request is made via HTMX, a partial HTML response for the posts or comments
                      is returned.

    Raises:
        Http404: If the profile of the specified user cannot be found or if the logged-in user does not have a profile.

    HTMX Options:
        - `top-posts`: Fetches posts sorted by the number of likes, displaying only posts with likes greater than zero.
        - `top-comments`: Fetches comments sorted by the number of likes, displaying only comments with likes greater than zero.
        - `liked-posts`: Fetches posts that the user has liked, ordered by the time they were liked.
    """
    if username:
        profile = get_object_or_404(User, username=username).profile
    else:
        try:
            profile = request.user.profile
        except:
            raise Http404("User not found")

    posts = profile.user.posts.all()

    if request.htmx:
        if "top-posts" in request.GET:
            posts = (
                profile.user.posts.annotate(num_likes=Count("likes"))
                .filter(num_likes__gt=0)
                .order_by("-num_likes")
            )
        elif "top-comments" in request.GET:
            comments = (
                profile.user.comments.annotate(num_likes=Count("likes"))
                .filter(num_likes__gt=0)
                .order_by("-num_likes")
            )
            replyform = ReplyCreateForm()
            return render(
                request,
                "snippets/loop_profile_comments.html",
                {"comments": comments, "replyform": replyform},
            )
        elif "liked-posts" in request.GET:
            posts = profile.user.likedposts.order_by("-likedpost__created")
        return render(request, "snippets/loop_profile_posts.html", {"posts": posts})

    context = {"profile": profile, "posts": posts}

    return render(request, "users/profile.html", context)


@login_required
def profile_edit_view(request: HttpRequest) -> HttpResponse:
    """
    Handle the profile edit functionality for the currently logged-in user.

    Args:
        request (HttpRequest): The HTTP request object containing user session data,
                               form data, and file uploads for profile editing.

    Returns:
        HttpResponse:
            - The rendered HTML template for profile editing (or onboarding) with the form.
            - A redirect to the profile page upon successful form submission.
    """
    form = ProfileForm(instance=request.user.profile)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect("profile")
    if request.path == reverse("profile-onboarding"):
        template = "users/profile_onboarding.html"
    else:
        template = "users/profile_edit.html"

    return render(request, template, {"form": form})


@login_required
def profile_delete_view(request: HttpRequest) -> HttpResponse:
    """
    Handle the deletion of the currently logged-in user's account.

    Args:
        request (HttpRequest): The HTTP request object containing user session and authentication data.

    Returns:
        HttpResponse:
            - A redirect to the home page if the profile deletion is successful (on POST request).
            - A rendered HTML response displaying the profile deletion confirmation page (on GET request).
    """
    user = request.user

    if request.method == "POST":
        logout(request)
        user.delete()
        messages.success(request, "Account deleted, what a pity")
        return redirect("home")

    return render(request, "users/profile_delete.html")
