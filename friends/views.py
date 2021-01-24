import json
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.http import JsonResponse
from django.views.generic import ListView
from .serializers import NotificationSerializer
from .models import *


class FindFriendsListView(ListView):
    model = Friend
    context_object_name = 'users'
    template_name = 'friends/find-friends.html'

    def get_queryset(self):
        current_user_friends = self.request.user.friends.values('id')
        sent_request = list(Friend.objects.filter(current_user=self.request.user).values_list('current_user_id',
                                                                                              flat=True))
        users = CustomUser.objects.exclude(id__in=current_user_friends).exclude(id__in=sent_request). \
            exclude(id=self.request.user.id)
        return users


def send_request(request, username=None):
    if username is not None:
        friend_user = CustomUser.objects.get(username=username)
        friend = Friend.objects.create(users=request.user, current_user=friend_user)
        notification = CustomNotification.objects.create(type="friend", recipient=friend_user,
                                                         actor=request.user, verb="sent you friend request")
        channel_layer = get_channel_layer()
        channel = "notifications_{}".format(friend_user.username)
        async_to_sync(channel_layer.group_send)(
            channel, {
                "type": "notify",
                "command": "new_notification",
                "notification": json.dumps(NotificationSerializer(notification).data)
            }
        )
        data = {
            'status': True,
            'message': "Request sent.",
        }
        return JsonResponse(data)
    else:
        pass


def accept_request(request, friend=None):
    if friend is not None:
        friend_user = CustomUser.objects.get(username=friend)
        current_user = request.user
        f = Friend.objects.filter(users=friend_user, current_user=current_user, status='requested')[0]
        f.status = "friend"
        f.save()
        CustomNotification.objects.filter(recipient=current_user, actor=friend_user).delete()
        data = {
            'status': True,
            'message': "You accepted friend request",
        }
        return JsonResponse(data)
