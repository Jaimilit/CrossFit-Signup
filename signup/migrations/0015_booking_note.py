# Generated by Django 3.2.22 on 2023-12-15 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0014_auto_20231212_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='note',
            field=models.TextField(blank=True, null=True, verbose_name='Any additional comments'),
        ),
    ]
