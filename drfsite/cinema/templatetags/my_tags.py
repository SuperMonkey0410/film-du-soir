from django import template
from cinema.models import Film, Genre, Director
from django.utils.http import urlencode

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

@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)