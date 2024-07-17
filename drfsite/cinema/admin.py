from django.contrib import admin
from .models import Director, Film, Genre, Grades, Nomination, Awards, Actor, Category, Country, MovieShots, Feedback
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class FilmAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Film
        fields = '__all__'


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthday')
    list_display_links = ('name',)
    search_fields = ('name', 'biography', 'birthday')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'director_name', 'genre_list', 'actors_list', 'country_list')
    list_display_links = ('title', 'director_name',)
    search_fields = ('title', 'director__name', 'actors')
    list_filter = ('genre', 'grade', 'awards', 'nomination', 'actors')
    prepopulated_fields = {'slug': ('title',)}
    form = FilmAdminForm

    def director_name(self, obj):
        if obj.director:
            return obj.director.name
        return "No director"  # если director равен None(если нет режиссера)

    def genre_list(self, obj):
        return ", ".join([genre.title for genre in obj.genre.all()])

    def actors_list(self, obj):
        return ", ".join([actor.name for actor in obj.actors.all()])

    def country_list(self, obj):
        return ", ".join([country.name for country in obj.country.all()])

    # actors_list.short_description = 'Actors'


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Grades)
class GradesAdmin(admin.ModelAdmin):
    list_display = ('title', 'marks')
    list_display_links = ('title', 'marks')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Nomination)
class NominationAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Awards)
class AwardsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthday', 'age')
    list_display_links = ('name',)
    search_fields = ('name', 'birthday',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_display_links = ('title',)
    search_fields = ('title',)
    prepopulated_fields = {'url': ('title',)}


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name', 'films')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ('image', 'film')
    list_filter = ('film',)


@admin.register(Feedback)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('film', 'name',)
    list_filter = ('film', 'name',)
