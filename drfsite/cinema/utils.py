from django.shortcuts import render
from django.db.models import Q
from .models import *


# def search(request):
#     """Поиск"""
#     queryset = request.GET.get