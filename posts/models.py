import uuid

from django.db import models


class Post(models.Model):
    """
    A model representing a blog post.

    Attributes:
        title (str): The title of the post, limited to 500 characters.
        image (str): A URL pointing to the post's associated image, limited to 500 characters.
        body (str): The main content of the post.
        created (datetime): The timestamp when the post was created, automatically set at creation.
        id (str): A unique identifier for the post, generated using UUID4.
    """

    title = models.CharField(max_length=500)
    image = models.URLField(max_length=500)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(
        max_length=100,
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False,
    )

    def __str__(self) -> str:
        """
        Return a string representation of the post.

        Returns:
            str: The title of the post.
        """
        return str(self.title)

    class Meta:
        ordering = ["-created"]
