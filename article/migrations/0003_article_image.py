# Generated by Django 5.0.6 on 2024-06-12 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to='article/%Y/%m/%d'),
        ),
    ]
