from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse

from .models import *
from .forms import UserLoginForm, RegistrationForm
from django.contrib import auth


def register(request, ):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('users:home'))

    else:
        form = RegistrationForm()
    context = {'form': form}

    return render(request, 'users/register.html', context=context)


def login(request):
    if request.method == 'POST':
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
    auth.logout(request)
    return redirect(reverse('cinema:home'))


def profile(request, ):
    pass
