# Generated by Django 5.0.6 on 2024-08-07 06:33

import ckeditor.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reaction_type', models.CharField(choices=[('Like', 'Like'), ('Dislike', 'Dislike'), ('Heart', 'Heart'), ('Unicorn', 'Unicorn'), ('Clap', 'Clap'), ('Fire', 'Fire')], max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scores', models.IntegerField(default=0)),
                ('image', models.ImageField(blank=True, default=None, upload_to='profiles')),
                ('backImage', models.ImageField(blank=True, default=None, upload_to='back_images')),
                ('bio', ckeditor.fields.RichTextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=168)),
                ('Twitter', models.CharField(blank=True, max_length=1000)),
                ('GitHub', models.CharField(blank=True, max_length=1000)),
                ('GitLub', models.CharField(blank=True, max_length=1000)),
                ('Linkedin', models.CharField(blank=True, max_length=1000)),
                ('Telegram', models.CharField(blank=True, max_length=1000)),
                ('website', models.URLField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('interests', models.ManyToManyField(blank=True, null=True, to='user.interest')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('skills', models.ManyToManyField(blank=True, null=True, to='user.skill')),
            ],
        ),
    ]
