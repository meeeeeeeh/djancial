from django.db import models
from accounts.models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="userprofile")
    profile_image = models.ImageField(upload_to='avatars', default='avatars/cover.png')
    phone = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=20, blank=True)
    about = models.TextField(max_length=56, blank=True)

    def __str__(self):
        return self.user


@receiver(post_save, sender=CustomUser)
def create_profile(sender, **kwargs):
    if kwargs.get('created', False):
        UserProfile.objects.create(user=kwargs['instance'])




