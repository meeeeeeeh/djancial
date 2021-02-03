from django.db import models
from accounts.models import CustomUser
from django.utils.timezone import now


class TodoList(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="todo")
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    created = models.DateField(default=now)
    date = models.DateField(default=now)
    status = models.CharField(max_length=20, default="in progress")

    def __str__(self):
        return self.title

