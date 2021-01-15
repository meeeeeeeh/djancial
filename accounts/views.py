from django.contrib import messages
from django.contrib.auth import views
from accounts.forms import *
from accounts.models import CustomUser
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic


class SigUpView(generic.CreateView):
    model = CustomUser
    form_class = SignUpForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:login')

    def get_success_url(self):
        return self.success_url

    def post(self, request, *args, **kwargs):
        if CustomUser.objects.filter(email=request.POST['email']).exists():
            messages.warning(request, 'Этот адрес уже используется.')
            return redirect('accounts:signup')

        form = SignUpForm(request.POST)
        #TODO createview tg
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password1')
            user.set_password(password)
            user.save()
            return redirect('accounts:login')
        else:
            print(form.errors)
            return render(request, 'accounts/signup.html', {'form': form})


class UserLoginView(views.LoginView):
    template_name = 'accounts/login.html'


def home(request):
    if not request.user.is_authenticated:
        return redirect(reverse_lazy('accounts:login'))

    return render(request, 'accounts/home.html')


# class UserLogoutView(generic.RedirectView):
#     url = reverse_lazy('accounts:home')
#
#     def get(self, request, *args, **kwargs):
#         auth.logout(request)
#         messages.success(request, 'Вы вышли из аккаунта.')
#         return super(UserLogoutView, self).get(request, *args, *kwargs)
