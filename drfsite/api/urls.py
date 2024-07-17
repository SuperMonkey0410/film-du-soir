from django.contrib import admin
from django.urls import path
# from cinema.views import DirectorApiView, FilmsApiView
from .views import DirectorViewSet, FilmsViewSet, DirectorCreateView, GenreViewSet, GradesViewSet
from rest_framework import routers
from django.urls import include
from rest_framework.routers import DefaultRouter

router = routers.DefaultRouter()
router.register(r'director', DirectorViewSet, basename='director', )
router.register(r'films', FilmsViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'grades', GradesViewSet)
#print(router.urls)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/director_create', DirectorCreateView.as_view())

    # path('api/v1/cinema_list', DirectorApiView.as_view()),
    # path('api/v2/upd_films/<int:pk>/', FilmsApiView.as_view())
]
