# Generated by Django 4.1.2 on 2023-03-08 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_location_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bus',
            name='availableCapacity',
        ),
    ]