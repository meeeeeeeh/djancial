# Generated by Django 3.1.5 on 2021-02-05 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_auto_20210203_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='date',
            field=models.DateField(default='02-05-2021'),
        ),
    ]
