from django.urls import path
from .models import *
from .views import *

app_name = 'users'
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout', logout, name='logout'),
    path('profile', profile, name='profile')
]