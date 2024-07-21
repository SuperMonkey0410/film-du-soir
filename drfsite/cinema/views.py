from django.db.models import Q
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import FeedbackForm
from django.core.paginator import Paginator


class MovieList(View):
    def get(self, request):
        movies = Film.objects.all().order_by("-id")  # order_by ("?") - Сортировка по рандому
        # genres = Genre.objects.all()  # my_tags.py
        paginator = Paginator(movies, 9)
        page = request.GET.get('page', 1)
        page_obj = paginator.page(page)  # Номер  отображаемой страницы
        context = {'movies': page_obj}
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


def filter_genre(request):
    director_list = request.GET.getlist("director")
    genre_list = request.GET.getlist("genre")

    queryset = Film.objects.all()

    if director_list:
        queryset = queryset.filter(director__in=director_list)

    if genre_list:
        for genre in genre_list:
            queryset = queryset.filter(genre=genre)

    return render(request, 'movies/filter.html', {'movies': queryset})
