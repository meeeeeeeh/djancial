# Generated by Django 3.1.5 on 2021-02-05 21:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0004_auto_20210205_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
