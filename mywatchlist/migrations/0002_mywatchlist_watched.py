# Generated by Django 4.1 on 2022-09-20 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mywatchlist',
            name='watched',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
