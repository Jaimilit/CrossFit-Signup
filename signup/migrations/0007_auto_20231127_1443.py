# Generated by Django 3.2.22 on 2023-11-27 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('signup', '0006_remove_workoutsession_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='workoutsession',
            name='attendees',
            field=models.ManyToManyField(blank=True, related_name='signed_up_for', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='workoutsession',
            name='content',
            field=models.TextField(default='Your default value here'),
        ),
        migrations.AddField(
            model_name='workoutsession',
            name='excerpt',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='workoutsession',
            name='featured_image',
            field=models.ImageField(default='placeholder.jpg', upload_to='workout_images/'),
        ),
        migrations.AddField(
            model_name='workoutsession',
            name='session_creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_sessions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='workoutsession',
            name='slug',
            field=models.SlugField(default='default-slug', max_length=200, unique=True),
        ),
    ]
