from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Имя')
    photo = models.ImageField(upload_to='media/%y/%m/%d/', verbose_name='Изображение')
    biography = models.TextField(blank=True, null=True, verbose_name='Биография')
    birthday = models.CharField(max_length=100, blank=True, null=True, verbose_name='Дата рождения')
    slug = models.SlugField(max_length=120, blank=True, null=True)
    films = models.ManyToManyField(to='Film', blank=True, verbose_name='Фильмы', related_name='my_films')
    best_films = models.ManyToManyField(to='Film', blank=True, verbose_name='Лучшие фильмы',
                                        related_name='my_best_films')

    class Meta:
        db_table = 'directors'
        verbose_name = 'Режиссёр'
        verbose_name_plural = 'Режиссёры'

    def __str__(self):
        return self.name


class Film(models.Model):
    director = models.ForeignKey(to='Director', on_delete=models.PROTECT, related_name='director_of_film', blank=True,
                                 null=True, verbose_name='Режиссёр')
    genre = models.ManyToManyField(to='Genre', related_name='my_genre', blank=True, verbose_name='Жанр')
    grade = models.ManyToManyField(to='Grades', related_name='my_grade', blank=True, verbose_name='Оценка')
    awards = models.ManyToManyField(to='Awards', related_name='my_awards', blank=True, verbose_name='Награды')
    nomination = models.ManyToManyField(to='Nomination', related_name='my_nomination', blank=True,
                                        verbose_name='Номинации')
    actors = models.ManyToManyField(to='Actor', verbose_name="актеры", blank=True, null=True, related_name="film_actor")
    category = models.ForeignKey(to='Category', blank=True, null=True, related_name='film_category',
                                 on_delete=models.CASCADE, verbose_name='Категория')
    title = models.CharField(max_length=120, blank=True, null=True, verbose_name='Название')
    poster = models.ImageField(upload_to='poster/%y/%m/%d/', verbose_name='Изображение')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    country = models.ManyToManyField(to='Country', verbose_name='Страна', blank=True, related_name='film_country', )
    trailer = models.URLField(blank=True, null=True, verbose_name='Трейлер')
    data_of_release = models.CharField(max_length=50, blank=True, null=True, verbose_name='Дата выхода')
    budget = models.CharField(max_length=30, blank=True, null=True, verbose_name='Бюджет')
    slug = models.SlugField(max_length=120, blank=True, null=True)

    class Meta:
        db_table = 'films'
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    """Создаём Симметричную связь, фильма к режиссёру(если мы отметили режиссёра фильма, у режиссёра он автоматически сохранится"""

    def save(self, *args, **kwargs):
        super(Film, self).save(*args, **kwargs)
        if self.director:
            self.director.films.add(self)

    def __str__(self):
        return self.title


class Genre(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True, verbose_name='Жанр')
    slug = models.SlugField(max_length=120, blank=True, null=True)

    class Meta:
        db_table = 'genres'
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.title


class Grades(models.Model):
    choices = [
        ('IMDB', 'IMDb'),
        ('KP', 'Кинопоиск')
    ]
    title = models.CharField(max_length=150, choices=choices, blank=True, null=True)
    marks = models.FloatField(verbose_name='Оценка')
    slug = models.SlugField(max_length=120, blank=True, null=True)

    class Meta:
        db_table = 'grades'
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'

    def __str__(self):
        return f'{self.title} : {self.marks}'


class Awards(models.Model):
    ceremony = models.CharField(max_length=120, blank=True, null=True, verbose_name='Церемония/Фестиваль')
    title = models.CharField(max_length=120, blank=True, null=True, verbose_name='Награда')
    slug = models.SlugField(max_length=120, blank=True, null=True)

    class Meta:
        db_table = 'awards'
        verbose_name = 'Награда'
        verbose_name_plural = 'Награды'

    def __str__(self):
        return self.title


class Nomination(models.Model):
    title = models.CharField(max_length=120, blank=True, null=True, verbose_name='Номинация')
    slug = models.SlugField(max_length=120, blank=True, null=True)

    class Meta:
        db_table = 'nomination'
        verbose_name = 'Награда'
        verbose_name_plural = 'Награды'

    def __str__(self):
        return self.title


class Actor(models.Model):
    """Актёр"""
    name = models.CharField(max_length=150, null=True, blank=True, verbose_name='Имя')
    photo = models.ImageField(upload_to='media/actors/')
    birthday = models.CharField(blank=True, null=True, verbose_name='Дата рождения')
    films = models.ManyToManyField(to='Film', related_name='actors_films', blank=True, null=True, verbose_name='Фильмы')
    age = models.IntegerField(blank=True, null=True, verbose_name='Возраст')
    slug = models.SlugField()

    class Meta:
        db_table = 'actors'
        verbose_name = 'Актёр'
        verbose_name_plural = 'Актёры'

    def __str__(self):
        return self.name

    """Создаём Симметричную связь, актёра к фильму"""

    def save(self, *args, **kwargs):
        super(Actor, self).save(*args, **kwargs)
        for film in self.films.all():
            film.actors.add(self)


class Category(models.Model):
    """Категории (кино/аниме/сериал)"""
    choices = [
        ('film', 'Фильм'),
        ('serial', 'Сериал'),
        ('cartoon', 'Мультфильм'),
        ('anime', 'Аниме'),
    ]
    title = models.CharField(null=True, blank=True, choices=choices, verbose_name='Категория')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Country(models.Model):
    """Страна"""
    choices = [
        ('Италия', 'Италия'),
        ('Франция', 'Франция'),
        ('США', 'США'),
        ('Дания', 'Дания'),
        ('Россия', 'Россия'),
        ('Япония', 'Япония'),
        ('Бельгия', 'Бельгия'),
        ('Германия', 'Германия'),
        ('Швеция', 'Швеция'),

    ]
    name = models.CharField(max_length=100, choices=choices, blank=True, null=True, verbose_name='Страна')
    films = models.ManyToManyField(to='Film', related_name='country_films', blank=True, null=True,
                                   verbose_name='Фильмы')
    slug = models.SlugField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'country'
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    """Создаём Симметричную связь, страны к фильму"""

    # def save(self, *args, **kwargs):
    #     super(Film, self).save(*args, **kwargs)
    #     if self.director:
    #         self.director.films.add(self)


class MovieShots(models.Model):
    """Кадры из фильма"""
    image = models.ImageField(null=True, blank=True, upload_to='media/movie_shots/', verbose_name='Изображение')
    film = models.ForeignKey(to='Film', verbose_name="Фильм", on_delete=models.CASCADE)

    def __str__(self):
        return self.film.title

    class Meta:
        verbose_name = "Кадр из фильма"
        verbose_name_plural = "Кадры из фильма"


class Feedback(models.Model):
    """Комментарии под фильм"""
    text = models.TextField(verbose_name='Комментарий')
    film = models.ForeignKey(to='Film', on_delete=models.CASCADE, verbose_name='Фильм')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    name = models.CharField(max_length=100, blank=True, null=True,
                            verbose_name='Имя')  # Для незарегистрированного юзера
    email = models.EmailField(blank=True,)  # Для незарегистрированного юзера

    def __str__(self):
        return f"{self.name} - {self.film}"

    class Meta:
        db_table = 'feedback'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
