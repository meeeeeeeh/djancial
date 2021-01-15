from django.urls import path
from django.contrib.auth.views import LogoutView
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('signup/', SigUpView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('accounts:login')), name='logout'),
    path('home/', home, name='home'),

]