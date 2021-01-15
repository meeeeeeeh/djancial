from django.db import models
from django.utils.timezone import now
from accounts.models import CustomUser


# TODO datetimeview
class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="posts")
    body = models.TextField()
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=now)
