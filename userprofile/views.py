from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView
from accounts.models import CustomUser
from userprofile.models import UserProfile


class TimeLineView(DetailView):
    model = CustomUser
    template_name = "userprofile/user-profile.html"
    slug = "username"
    slug_url_kwarg = "username"
    context_object_name = "user"
    object = None

    def get_object(self, queryset=None):
        return self.model.objects.select_related("userprofile").prefetch_related("posts").get(
            username=self.kwargs.get(self.slug_url_kwarg))

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class ProfileEditView(UpdateView):
    model = UserProfile
    template_name = "userprofile/edit-profile.html"
    context_object_name = "userprofile"
    object = None
    fields = "__all__"

    def get_object(self, queryset=None):
        return self.request.user.userprofile

    # TODO put patch updateview
    def post(self, request, *args, **kwargs):
        print(request.POST.get('first_name'))
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.save()
        userprofile = user.userprofile
        userprofile.country = request.POST.get('country')
        userprofile.city = request.POST.get('city')
        userprofile.phone = request.POST.get('phone')
        userprofile.about = request.POST.get('about')
        userprofile.save()
        return redirect(reverse_lazy('userprofile:edit-profile'))
