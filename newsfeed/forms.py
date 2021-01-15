from django import forms
from newsfeed.models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("body",)
