import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe

from accounts.models import CustomUser
from friends.models import Friend


def all_messages(request):
    friends_one = Friend.objects.filter(users=request.user, status='friend')
    friends_two = Friend.objects.filter(current_user=request.user, status='friend')
    friends = friends_one | friends_two
    return render(request, "communications/all-messages.html", {'friends': friends})


@login_required(login_url=reverse_lazy("accounts:login"))
def messages_with_one_friend(request, username):
    if request.user.username == username:
        return redirect(reverse_lazy('communications:all-messages'))
    try:
        if not CustomUser.objects.get(username=username):
            return redirect(reverse_lazy('communications:all-messages'))
    except:
        return redirect(reverse_lazy('communications:all-messages'))
    friends_one = Friend.objects.filter(users=request.user, status='friend')
    friends_two = Friend.objects.filter(current_user=request.user, status='friend')
    friends = friends_one | friends_two
    return render(request, "communications/friend-messages.html", {
        'friends': friends,
        'friend_name_json': mark_safe(json.dumps(username)),
        'username': mark_safe(json.dumps(request.user.username)),
    })
