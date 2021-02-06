from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import TodoList
from .forms import ToDoCreateFrom
from django.shortcuts import get_object_or_404
from .tasks import send_notification_email
from datetime import datetime


class ToDoCreateView(CreateView):
    model = TodoList
    http_method_names = ['post']
    form_class = ToDoCreateFrom
    template_name = "todo.html"
    success_url = reverse_lazy("todo:todo")

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
        return super(ToDoCreateView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return redirect(reverse_lazy("todo:todo"))

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        self.object = None
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


def todo(request):
    if not request.user.is_authenticated:
        return redirect(reverse_lazy('accounts:login'))
    todos = TodoList.objects.filter(user=request.user)
    return render(request, 'todo/todo.html', {'todos': todos})


def delete_todo(request, pk):
    get_object_or_404(TodoList, pk=pk).delete()
    return redirect('todo:todo')


send_notification_email.delay()
