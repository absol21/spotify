# Generated by Django 4.2.1 on 2023-06-13 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='description',
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='image',
        ),
    ]