from django.shortcuts import render


def home_view(request):
    """
    View function that renders the index.html template.

    Args:
        request: The HTTP request object that contains metadata about the request.

    Returns:
        HttpResponse: A rendered HTML response with the context data passed to the template.
    """
    return render(request, "posts/home.html")
