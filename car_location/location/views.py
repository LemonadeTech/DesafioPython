from car_location.core.forms import LoginForm
from car_location.location.api_view_rest import CategoriaVeiculoViewSet
from car_location.location.models.categoriaveiculo import CategoriaVeiculo
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url as r
import json
import requests

def home(request):
    return render(request, 'base.html')


def categoria(request):

    url = r('location:categoriaveiculo-list')
    response = requests.get(request.META['wsgi.url_scheme']+'://'+request.get_host() + url)
    data = json.loads(response.text)
    categoria_veiculos = []
    for d in data:
        categoria_veiculos.append(CategoriaVeiculo(**d))
    context = {'categorias': categoria_veiculos}
    return render(request, 'categoria_veiculo/categoria_veiculos_list.html', context)


def categoria_new(request):

    if request.method == 'GET':
        context = {'label': 'Cadastrar'}
        return render(request, 'categoria_veiculo/categoria_veiculos.html', context)


    data = dict(request.POST)
    data.pop('csrfmiddlewaretoken')
    if data['pk'][0] == '':
        url = r('location:categoriaveiculo-list')
        data.pop('pk')
        msg = 'Cadastro realizado com sucesso!!'
        response = requests.post(request.META['wsgi.url_scheme']+'://'+request.get_host() + url, data=data)
    else:
        url = r('location:categoriaveiculo-detail', data['pk'][0])
        response = requests.put(request.META['wsgi.url_scheme']+'://'+request.get_host() + url, data=data)
        msg = 'Categoria atualizada com sucesso!!'

    messages.success(request, msg)
    return HttpResponseRedirect(r('categoria'))

def categoria_detail(request, pk):
    url = r('location:categoriaveiculo-detail', pk)
    response = requests.get(request.META['wsgi.url_scheme']+'://'+request.get_host() + url)
    data = json.loads(response.text)
    categoria_veiculo = CategoriaVeiculo(**data)
    context = {'categoria': categoria_veiculo, 'label': 'Editar'}

    return render(request, 'categoria_veiculo/categoria_veiculos.html', context)


def veiculo(request):
    return render(request, 'categoria_veiculo/categoria_veiculos.html')

def cliente(request):
    return render(request, 'categoria_veiculo/categoria_veiculos.html')

def locacao(request):
    return render(request, 'categoria_veiculo/categoria_veiculos.html')

def devolucao(request):
    return render(request, 'categoria_veiculo/categoria_veiculos.html')

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