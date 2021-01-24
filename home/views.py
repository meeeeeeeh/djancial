from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from friends.models import Friend
from newsfeed.models import Post


def home(request):
    if not request.user.is_authenticated:
        return redirect(reverse_lazy('accounts:login'))

    friends_one = Friend.objects.filter(users=request.user).filter(status='friend')
    friends_two = Friend.objects.filter(current_user=request.user).filter(status='friend')
    friends_list_one = list(friends_one.values_list('users_id', flat=True))
    friends_list_two = list(friends_two.values_list('current_user_id', flat=True))
    friends_list_id = friends_list_one + friends_list_two + [request.user.id]
    friends = friends_one.union(friends_two)
    posts = Post.objects.all()
    return render(request, 'accounts/home.html', {'posts': posts, 'friends': friends})





