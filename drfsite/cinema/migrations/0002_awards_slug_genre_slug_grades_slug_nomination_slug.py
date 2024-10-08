# Generated by Django 5.0.4 on 2024-04-25 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='awards',
            name='slug',
            field=models.SlugField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='genre',
            name='slug',
            field=models.SlugField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='grades',
            name='slug',
            field=models.SlugField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='nomination',
            name='slug',
            field=models.SlugField(blank=True, max_length=120, null=True),
        ),
    ]
