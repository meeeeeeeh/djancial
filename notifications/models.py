from django.db import models
from accounts.models import CustomUser
from todolist.models import TodoList


class Notification(models.Model):
    todo = models.ForeignKey(TodoList, on_delete=models.CASCADE,
                             blank=True, null=True, related_name="todo_notification")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user_notifications")
    created_at = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

