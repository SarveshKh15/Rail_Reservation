# Generated by Django 3.2.12 on 2024-04-07 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20240407_1442'),
    ]

    operations = [
        migrations.RenameField(
            model_name='route',
            old_name='Dstation',
            new_name='dstation',
        ),
        migrations.RenameField(
            model_name='route',
            old_name='Ostation',
            new_name='ostation',
        ),
    ]
