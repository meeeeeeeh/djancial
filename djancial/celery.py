import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djancial.settings')

app = Celery('djancial')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'send-notification': {
        'task': 'todolist.tasks.send_notification_email',
        'schedule': crontab(minute='*/10'),
    }
}