# Generated by Django 3.2.12 on 2024-04-07 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_account_clein'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.clein'),
        ),
    ]
