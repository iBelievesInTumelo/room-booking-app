# Generated by Django 5.0.4 on 2024-07-04 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_booking_room_bookings_room_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='image',
            field=models.URLField(),
        ),
    ]