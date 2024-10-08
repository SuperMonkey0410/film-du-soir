# Generated by Django 5.0.4 on 2024-07-05 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0017_alter_film_poster'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('Italy', 'Италия'), ('France', 'Франция'), ('USA', 'США'), ('Denmark', 'Дания'), ('Russia', 'Россия'), ('Japan', 'Япония'), ('Belgium', 'Бельгия')], max_length=100, null=True, verbose_name='Страна')),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='country',
            field=models.ManyToManyField(blank=True, related_name='film_country', to='cinema.country', verbose_name='Страна'),
        ),
    ]
