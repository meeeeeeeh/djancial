from django.urls import path
from .views import *
from search.views import search

app_name = 'friends'

urlpatterns = [
    path('find-friends', FindFriendsListView.as_view(), name="find-friends"),
    path('accept-friends', AcceptFriendsListView.as_view(), name="accept-friends"),
    path('send-request/<slug:username>', send_request, name="send-request"),
    path('accept-request/<slug:friend>', accept_request, name="accept-request"),
    path('search/', search, name='search'),

]