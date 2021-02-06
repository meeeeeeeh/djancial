from django.core.mail import send_mail
from djancial.celery import app
from .models import TodoList
from datetime import datetime


@app.task
def send_notification_email():
    for todo_item in TodoList.objects.filter(date=datetime.now()):
        send_mail(
            todo_item.title,
            todo_item.content,
            'testmail123qweasd@gmail.com',
            [todo_item.user.email],
            fail_silently=False,
        )
        todo_item.status = "notified"
        todo_item.save()
