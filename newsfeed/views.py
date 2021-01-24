from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from newsfeed.forms import PostCreateForm
from newsfeed.models import *


class PostCreateView(CreateView):
    model = Post
    http_method_names = ['post']
    form_class = PostCreateForm
    template_name = 'home.html'
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super(PostCreateView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return redirect(reverse_lazy('home:home'))

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        self.object = None
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


# TODO createview
def create_comment(request, post_id=None):
    if request.method == "POST":
        post = Post.objects.get(id=post_id)
        comment = post.comments.create(user=request.user, content=request.POST.get('content'))
        return redirect(reverse_lazy('home:home'))
    else:
        return redirect(reverse_lazy('home:home'))
