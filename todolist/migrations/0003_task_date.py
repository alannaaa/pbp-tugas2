# Generated by Django 4.1 on 2022-09-26 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_remove_task_date_task_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
