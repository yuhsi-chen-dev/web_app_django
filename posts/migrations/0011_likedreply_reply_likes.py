# Generated by Django 5.1.4 on 2025-01-13 08:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0010_likedcomment_comment_likes"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="LikedReply",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "reply",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="posts.reply"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="reply",
            name="likes",
            field=models.ManyToManyField(
                related_name="likedreplies",
                through="posts.LikedReply",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
