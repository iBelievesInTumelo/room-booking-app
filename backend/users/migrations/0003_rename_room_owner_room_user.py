# Generated by Django 5.0.4 on 2024-06-18 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_room_bookings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='room_owner',
            new_name='user',
        ),
    ]
