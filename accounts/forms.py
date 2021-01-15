from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser


class SignUpForm(UserCreationForm):
    GENDER_CHOICE = (
        ("Male", "Мужской"),
        ("Female", "Женский")
    )
    username = forms.CharField(label="Имя пользователя")
    email = forms.EmailField(label="E-mail")
    gender = forms.ChoiceField(choices=GENDER_CHOICE, label="Пол")
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'gender',
            'password1',
            'password2',
        )


# class UserLoginForm(forms.Form):
#     email = forms.EmailField(label="E-mail")
#     password = forms.CharField(label="Пароль", strip=False, widget=forms.PasswordInput())
#
#     class Meta:
#         model = CustomUser
#         fields = (
#             'email',
#             'password',
#         )
