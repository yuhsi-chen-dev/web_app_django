import uuid

from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    """
    A model representing a blog post.

    Attributes:
        title (str): The title of the post, limited to 500 characters.
        artist (str): The creator of the image on Flickr, limited to 500 characters.
        url (str): The url of the image on Flickr, limited to 500 characters.
        image (str): A URL pointing to the post's associated image, limited to 500 characters.
        author (ForeignKey): A foreign key relationship to the `User` model.
        body (str): The main content of the post.
        likes (ManyToManyField): A many-to-many relationship with the `User` model,
            indicating which users have liked the post. The relationship is managed
            through the `LikedPost` intermediate model.
        tags (ManyToManyField): A many-to-many relationship with the `Tag` model,
            allowing multiple tags to be associated with a post.
        created (datetime): The timestamp when the post was created, automatically set at creation.
        id (str): A unique identifier for the post, generated using UUID4.

    Methods:
        __str__():
            Returns a string representation of the post, typically the title.
    """

    title = models.CharField(max_length=500)
    artist = models.CharField(max_length=500, null=True)
    url = models.URLField(max_length=500, null=True)
    image = models.URLField(max_length=500)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="posts"
    )
    body = models.TextField()
    likes = models.ManyToManyField(User, related_name="likedposts", through="LikedPost")
    tags = models.ManyToManyField("Tag")
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


class LikedPost(models.Model):
    """
    A model representing a user liking a post.

    Attributes:
        user (ForeignKey): A foreign key relationship to the `User` model,
            indicating the user who liked the post.
        post (ForeignKey): A foreign key relationship to the `Post` model,
            indicating the post that was liked.
        created (datetime): The timestamp when the post was liked, automatically set at creation.

    Methods:
        __str__():
            Returns a string representation of the liked post, typically the post's title.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """
        Return a string representation of the liked post.

        Returns:
            str: The title of the liked post.
        """
        return f"{self.user.username} : {self.post.title}"


class Tag(models.Model):
    """
    Represents a tag that can be associated with multiple blog posts.

    Attributes:
        name (str): The name of the tag, with a maximum length of 20 characters.
        slug (str): A unique slug identifier for the tag, used for URLs
            or referencing tags in a more readable format.
        order (int, optional): A numeric value used to define the display order
            of tags. Tags with lower values are displayed first. Can be null.

    Methods:
        __str__():
            Returns the name of the tag as its string representation.
    """

    name = models.CharField(max_length=20)
    image = models.FileField(upload_to="icons/", null=True, blank=True)
    slug = models.SlugField(max_length=20, unique=True)
    order = models.IntegerField(null=True)

    def __str__(self) -> str:
        """
        Return a string representation of the tag.

        Returns:
            str: The name of the tag.
        """
        return str(self.name)

    class Meta:
        ordering = ["order"]


class Comment(models.Model):
    """
    Represents a comment made on a blog post.

    Attributes:
        author (ForeignKey): A foreign key relationship to the `User` model,
            indicating the user who made the comment. Can be null if the user is deleted.
        parent_post (ForeignKey): A foreign key relationship to the `Post` model,
            indicating the post that the comment is associated with. Deleting the post
            will delete all associated comments.
        body (str): The text content of the comment, with a maximum length of 150 characters.
        likes (ManyToManyField): A many-to-many relationship with the `User` model,
            indicating which users have liked the comment. The relationship is managed
            through the `LikedComment` intermediate model.
        created (datetime): The timestamp when the comment was created,
            automatically set at creation.
        id (str): A unique identifier for the comment, generated using UUID4.

    Methods:
        __str__():
            Returns a string representation of the comment, typically in the format:
            "<author.username>: <first 30 characters of body>".
    """

    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="comments"
    )
    parent_post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    body = models.CharField(max_length=150)
    likes = models.ManyToManyField(
        User, related_name="likedcomments", through="LikedComment"
    )
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
        Return a string representation of the comment.

        Returns:
            str: A formatted string containing the author's username and
                 the first 30 characters of the comment body. If the author
                 is None, 'Anonymous' is used instead of the username.
        """
        try:
            return f"{self.author.username} : {self.body[:30]}"
        except:
            return f"Anonymous : {self.body[:30]}"

    class Meta:
        ordering = ["-created"]


class LikedComment(models.Model):
    """
    A model representing a user liking a comment.

    Attributes:
        user (ForeignKey): A foreign key relationship to the `User` model,
            indicating the user who liked the post.
        comment (ForeignKey): A foreign key relationship to the `Comment` model,
            indicating the comment that was liked.
        created (datetime): The timestamp when the comment was liked, automatically set at creation.

    Methods:
        __str__():
            Returns a string representation of the liked comment, typically the comment's body.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """
        Return a string representation of the liked comment.

        Returns:
            str: The body of the liked comment.
        """
        return f"{self.user.username} : {self.comment.body[:30]}"


class Reply(models.Model):
    """
    Represents a reply to a comment on a blog post.

    Attributes:
        author (ForeignKey): A foreign key relationship to the `User` model,
            indicating the user who made the reply. Can be null if the user is deleted.
        parent_comment (ForeignKey): A foreign key relationship to the `Comment` model,
            indicating the comment that the reply is associated with. Deleting the comment
            will delete all associated replies.
        body (str): The text content of the reply, with a maximum length of 150 characters.
        likes (ManyToManyField): A many-to-many relationship with the `User` model,
            indicating which users have liked the reply. The relationship is managed
            through the `LikedReply` intermediate model.
        created (datetime): The timestamp when the reply was created, automatically set at creation.
        id (str): A unique identifier for the reply, generated using UUID4.

    Methods:
        __str__():
            Returns a string representation of the reply, typically in the format:
            "<author.username>: <first 30 characters of body>".
    """

    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="replies"
    )
    parent_comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name="replies"
    )
    body = models.CharField(max_length=150)
    likes = models.ManyToManyField(
        User, related_name="likedreplies", through="LikedReply"
    )
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
        Return a string representation of the reply.

        Returns:
            str: A formatted string containing the author's username and
                 the first 30 characters of the reply body. If the author
                 is None, 'Anonymous' is used instead of the username.
        """
        try:
            return f"{self.author.username} : {self.body[:30]}"
        except:
            return f"Anonymous : {self.body[:30]}"

    class Meta:
        ordering = ["-created"]


class LikedReply(models.Model):
    """
    A model representing a user liking a reply.

    Attributes:
        user (ForeignKey): A foreign key relationship to the `User` model,
            indicating the user who liked the reply.
        comment (ForeignKey): A foreign key relationship to the `Reply` model,
            indicating the reply that was liked.
        created (datetime): The timestamp when the reply was liked, automatically set at creation.

    Methods:
        __str__():
            Returns a string representation of the liked reply, typically the reply's body.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """
        Return a string representation of the liked reply.

        Returns:
            str: The body of the liked reply.
        """
        return f"{self.user.username} : {self.reply.body[:30]}"
