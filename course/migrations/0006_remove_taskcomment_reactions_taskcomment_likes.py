# Generated by Django 5.0.6 on 2024-06-19 17:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_task_reactions_taskcomment_reactions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskcomment',
            name='reactions',
        ),
        migrations.AddField(
            model_name='taskcomment',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='articleLikes', to=settings.AUTH_USER_MODEL),
        ),
    ]
