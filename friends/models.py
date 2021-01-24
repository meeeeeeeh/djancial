from django.db import models
from accounts.models import CustomUser
from django.conf import settings
from django.utils.timezone import now


class Friend(models.Model):
    users = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    current_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='friends', null=True)
    status = models.CharField(max_length=20, default='requested')
    created_at = models.DateTimeField(default=now)


class CustomNotification(models.Model):
    type = models.CharField(default='friend', max_length=30)

    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, related_name='notifications',
                                  on_delete=models.CASCADE)
    unread = models.BooleanField(default=True, blank=False, db_index=True)

    actor = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, on_delete=models.CASCADE)

    verb = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(default=now, db_index=True)
    deleted = models.BooleanField(default=False, db_index=True)
    emailed = models.BooleanField(default=False, db_index=True)
