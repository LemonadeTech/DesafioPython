from car_location.core.forms import LoginForm
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url as r


@login_required
def home(request):
    return render(request, 'base.html')


def do_logout(request):
    logout(request)
    return HttpResponseRedirect(r('/'))


def do_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(r('home'))

    log_form = LoginForm(request.POST)

    if request.method == 'GET'or not log_form.is_valid():
        return render(request, 'login/login.html', {'form': LoginForm()})


    username = log_form.cleaned_data['username']
    password = log_form.cleaned_data['password']

    try:
        u = User.objects.get(username=username)
    except ObjectDoesNotExist:
        messages.error(request,  'Usuário ou senha inválidos')
        return render(request, 'login/login.html', {'form': LoginForm()})

    usuario = authenticate(username=username, password=password)
    login(request, usuario)

    return HttpResponseRedirect(r('home'))