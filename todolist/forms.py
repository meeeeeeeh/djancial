from django import forms
from todolist.models import TodoList


class ToDoCreateFrom(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = (
            "title",
            "content",
            "date",
        )
