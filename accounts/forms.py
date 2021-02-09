from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser


class SignUpForm(UserCreationForm):
    GENDER_CHOICE = (
        ("Male", "Male"),
        ("Female", "Female")
    )
    username = forms.CharField(label="Username")
    email = forms.EmailField(label="E-mail")
    gender = forms.ChoiceField(choices=GENDER_CHOICE, label="Gender")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput())

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
#     password = forms.CharField(label="Password", strip=False, widget=forms.PasswordInput())
#
#     class Meta:
#         model = CustomUser
#         fields = (
#             'email',
#             'password',
#         )
