# Generated by Django 4.2 on 2023-04-21 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_chat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='from_yoga',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='from_zumba',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='to_yoga',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='to_zumba',
        ),
    ]
