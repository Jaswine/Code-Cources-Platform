# Generated by Django 4.1.4 on 2023-01-20 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_remove_course_commentscount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursetask',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='courses/tasks/videos'),
        ),
    ]
