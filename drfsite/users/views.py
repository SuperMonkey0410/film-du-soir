from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from .models import *
from .forms import UserLoginForm
from django.contrib import auth


def register(request, ):
    return render(request, 'users/register.html', )


def login(request, ):
    form = UserLoginForm(data=request.POST)
    if form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('cinema:home'))
    else:
        form = UserLoginForm()

    context = {'form': form}
    return render(request, 'users/login.html', context=context)


def logout(request, ):
    pass


def profile(request, ):
    pass
