from django.urls import path
from .views import *

app_name = 'cinema'
urlpatterns = [
    path('', MovieList.as_view(), name='home'),
    path('filter/', filter_genre, name='filter'),
    path('detail/<slug:slug_id>', MovieDetail.as_view(), name='movie_detail'),
    path('comment/<int:pk>', AddReview.as_view(), name='comment'),
    path('director/<slug:slug_id>', get_director, name='director'),
]
