from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from cinema.models import Director, Film, Genre, Grades, Actor
from .serializers import DirectorSerializer, FilmSerializer, GenreSerializer, GradesSerializer


# Create your views here.
class FilmsViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    @action(methods=['get', ], detail=False, url_path='last-films')
    def last_films(self, request):
        last_films = Film.objects.all()[:1]
        serializer = self.get_serializer(last_films, many=True)
        return Response(serializer.data)

    @action(methods=['get', ], detail=False, url_path='lynch-films-title')
    def lynch_films(self, request):
        name = Director.objects.get(name='Дэвид Линч')
        lynch_films = Film.objects.filter(director=name)
        serializer = self.get_serializer(lynch_films, many=True)
        return Response(serializer.data)

class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

    @action(methods=['get', 'post'], detail=False)
    def films(self, request):
        films = Film.objects.all()
        return Response({'films': [f.title for f in films]})


class DirectorCreateView(generics.CreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GradesViewSet(viewsets.ModelViewSet):
    queryset = Grades.objects.all()
    serializer_class = GradesSerializer

# class DirectorApiView(generics.ListCreateAPIView):
#     queryset = Director.objects.all()
#     serializer_class = DirectorSerializer
#
#
#
# class FilmsApiView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = FilmSerializer
#     queryset = Film.objects.all()
