# Generated by Django 3.2.22 on 2023-11-27 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0008_auto_20231127_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='workoutsession',
            name='day',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], default='Monday', max_length=20),
        ),
    ]
