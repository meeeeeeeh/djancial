from django.urls import path
from .views import *

app_name = "todo"

urlpatterns = [
    path('todo', todo, name="todo"),
    path('todo/create', ToDoCreateView.as_view(), name="todo-create"),
    path('todo/delete/<int:pk>', delete_todo, name="todo-delete"),
]
