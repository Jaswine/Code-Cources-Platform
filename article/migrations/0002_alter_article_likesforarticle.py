# Generated by Django 4.1.7 on 2023-04-16 07:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='likesForArticle',
            field=models.ManyToManyField(blank=True, default=[], related_name='likesForArticle', to=settings.AUTH_USER_MODEL),
        ),
    ]
