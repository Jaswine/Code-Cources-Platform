# Generated by Django 5.0.6 on 2024-06-20 07:12

import course.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_alter_taskcomment_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='video',
            field=models.FileField(blank=True, upload_to=course.models.Task.task_directory_path),
        ),
    ]