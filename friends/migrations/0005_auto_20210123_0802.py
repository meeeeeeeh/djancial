# Generated by Django 3.1.5 on 2021-01-23 08:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('friends', '0004_auto_20210123_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='current_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='friends', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='friend',
            name='users',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
