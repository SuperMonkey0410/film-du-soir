# Generated by Django 5.0.4 on 2024-07-09 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0023_movieshots'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movieshots',
            old_name='movie',
            new_name='film',
        ),
    ]
