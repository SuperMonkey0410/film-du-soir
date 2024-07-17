from django import template
from cinema.models import Film, Genre, Director

register = template.Library()


@register.simple_tag()
def get_genres():
    genres = Genre.objects.all()
    return genres


@register.simple_tag()
def get_directors():
    directors = Director.objects.all()
    return directors


@register.inclusion_tag('movies/includes/last_films.html')
def get_last_films(count=4):
    latest_films = Film.objects.order_by("-id")[:count]
    return {'latest_films': latest_films}
