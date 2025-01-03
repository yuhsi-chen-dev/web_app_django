from django.shortcuts import render


def home_view(request):
    """
    View function that renders the index.html template with a dynamic title.

    Args:
        request: The HTTP request object that contains metadata about the request.

    Returns:
        HttpResponse: A rendered HTML response with the context data passed to the template.
    """
    title = "Welcome to Django"
    return render(request, "index.html", {"title": title})
