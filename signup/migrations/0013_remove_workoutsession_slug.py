# Generated by Django 3.2.22 on 2023-12-01 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0012_alter_booking_workout_session'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workoutsession',
            name='slug',
        ),
    ]
