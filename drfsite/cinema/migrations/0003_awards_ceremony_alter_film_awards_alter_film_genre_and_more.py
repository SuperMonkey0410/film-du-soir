# Generated by Django 5.0.4 on 2024-04-25 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0002_awards_slug_genre_slug_grades_slug_nomination_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='awards',
            name='ceremony',
            field=models.CharField(blank=True, max_length=120, null=True, verbose_name='Церемония/Фестиваль'),
        ),
        migrations.AlterField(
            model_name='film',
            name='awards',
            field=models.ManyToManyField(blank=True, related_name='my_awards', to='cinema.awards'),
        ),
        migrations.AlterField(
            model_name='film',
            name='genre',
            field=models.ManyToManyField(blank=True, related_name='my_genre', to='cinema.genre'),
        ),
        migrations.AlterField(
            model_name='film',
            name='grade',
            field=models.ManyToManyField(blank=True, related_name='my_grade', to='cinema.grades'),
        ),
        migrations.AlterField(
            model_name='film',
            name='nomination',
            field=models.ManyToManyField(blank=True, related_name='my_nomination', to='cinema.nomination'),
        ),
    ]
