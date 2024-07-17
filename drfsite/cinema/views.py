from django.db.models import Q
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import FeedbackForm


class MovieList(View):
    def get(self, request):
        movies = Film.objects.all().order_by("-id")  # order_by ("?") - Сортировка по рандому
        # genres = Genre.objects.all()  # my_tags.py
        context = {'movies': movies}  # 'genres': genres}
        return render(request, 'movies/movie_list.html', context=context)


class MovieDetail(View):
    def get(self, request, slug_id):
        movie = Film.objects.get(slug=slug_id)
        genres = Genre.objects.all()
        context = {"movie": movie, 'genres': genres}
        return render(request, 'movies/movie_detail.html', context=context)


class AddReview(View):
    """Отзывы"""
    def post(self, request, pk):
        form = FeedbackForm(request.POST)
        movie = Film.objects.get(id=pk)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.film_id = movie.id  # Присваиваем значение поля "film_id"
            feedback.save()
        return redirect('/')


def get_director(request, slug_id):
    """Страница с режиссёрами, может стоит убрать ее в templatetags?"""
    director = Director.objects.get(slug=slug_id)
    films = director.films.all()
    context = {'director': director, 'films': films}
    return render(request, 'movies/directors.html', context=context)


def filter_genre(request, genre_slug):
    genres = Film.objects.filter(genre__in=request.GET.get('genre'))
    context = {'genre': genres}
    return render(request, )
