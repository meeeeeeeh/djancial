from django.urls import path
from userprofile.views import *

app_name = "userprofile"

urlpatterns = [
    path('edit-profile', ProfileEditView.as_view(), name="edit-profile"),
    path('profile/<slug:username>', TimeLineView.as_view(), name="user-timeline"),
]