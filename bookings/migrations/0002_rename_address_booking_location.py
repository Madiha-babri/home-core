# Generated by Django 4.2.17 on 2025-01-05 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='address',
            new_name='location',
        ),
    ]
