# Generated by Django 3.2.12 on 2024-04-07 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_rename_tno_reservation_tname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='amt',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='status',
        ),
    ]
