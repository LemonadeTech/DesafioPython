from car_location.core.forms import LoginForm
from car_location.location.forms import CategoriaVeiculoForm, VeiculoForm, \
    ClienteForm, LocacaoForm, DevolucaoForm, ReservaForm
from car_location.location.models.categoriaveiculo import CategoriaVeiculo
from car_location.location.models.cliente import Cliente
from car_location.location.models.devolucao import Devolucao
from car_location.location.models.locacao import Locacao
from car_location.location.models.reserva import Reserva
from car_location.location.models.veiculo import Veiculo
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, resolve_url as r, get_object_or_404, \
    redirect
import json
from django.template.loader import render_to_string
import requests
from utils.mail_sender import MailSender


def home(request):
    return render(request, 'base.html')


def categoria_list(request):
    categoria_veiculos = CategoriaVeiculo.objects.all()
    context = {'categorias': categoria_veiculos}
    return render(request, 'categoria_veiculo/categoria_veiculos_list.html', context)


def categoria_new(request):

    if request.method == 'GET':
        context = {'label': 'Cadastrar', 'form': CategoriaVeiculoForm()}
        return render(request, 'categoria_veiculo/categoria_veiculos.html', context)

    form = CategoriaVeiculoForm(request.POST)
    context = {'label': 'Cadastrar', 'form': form}

    if not form.is_valid():
        return render(request, 'categoria_veiculo/categoria_veiculos.html', context)

    CategoriaVeiculo.objects.create(**form.cleaned_data)

    msg = 'Cadastro realizado com sucesso!!'
    messages.success(request, msg)
    return HttpResponseRedirect(r('categoria'))

def categoria_edit(request, pk):
    cat = get_object_or_404(CategoriaVeiculo, pk=pk)
    if request.method == "POST":
        form = CategoriaVeiculoForm(request.POST, instance=cat)
        if form.is_valid():
            cat = form.save(commit=False)
            cat.save()
            msg = 'Update realizado com sucesso!!'
            messages.success(request, msg)
            return HttpResponseRedirect(r('categoria'))
    else:
        form = CategoriaVeiculoForm(instance=cat)

    context = {'label': 'Editar', 'form': form}
    return render(request, 'categoria_veiculo/categoria_veiculos.html', context)


def veiculo_list(request):
    veiculos = Veiculo.objects.all()
    context = {'veiculos': veiculos}
    return render(request, 'veiculo/veiculos_list.html', context)

def veiculo_new(request):
    if request.method == 'GET':
        context = {'label': 'Cadastrar', 'form': VeiculoForm()}
        return render(request, 'veiculo/veiculos.html', context)

    form = VeiculoForm(request.POST)
    context = {'label': 'Cadastrar', 'form': form}

    if not form.is_valid():
        return render(request, 'veiculo/veiculos.html', context)

    Veiculo.objects.create(**form.cleaned_data)

    msg = 'Cadastro realizado com sucesso!!'
    messages.success(request, msg)
    return HttpResponseRedirect(r('veiculo'))

def veiculo_edit(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    if request.method == "POST":
        form = VeiculoForm(request.POST, instance=veiculo)
        if form.is_valid():
            veiculo = form.save(commit=False)
            veiculo.save()
            msg = 'Update realizado com sucesso!!'
            messages.success(request, msg)
            return HttpResponseRedirect(r('veiculo'))
    else:
        form = VeiculoForm(instance=veiculo)

    context = {'label': 'Editar', 'form': form}
    return render(request, 'veiculo/veiculos.html', context)


def cliente_list(request):
    clientes = Cliente.objects.all()
    context = {'clientes': clientes}
    return render(request, 'cliente/clientes_list.html', context)


def cliente_edit(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            msg = 'Update realizado com sucesso!!'
            messages.success(request, msg)
            return HttpResponseRedirect(r('cliente'))
    else:
        form = ClienteForm(instance=cliente)

    context = {'label': 'Editar', 'form': form}
    return render(request, 'cliente/clientes.html', context)

def cliente_new(request):
    if request.method == 'GET':
        context = {'label': 'Cadastrar', 'form': ClienteForm()}
        return render(request, 'cliente/clientes.html', context)

    form = ClienteForm(request.POST)
    context = {'label': 'Cadastrar', 'form': form}

    if not form.is_valid():
        return render(request, 'cliente/clientes.html', context)

    Cliente.objects.create(**form.cleaned_data)

    msg = 'Cadastro realizado com sucesso!!'
    messages.success(request, msg)
    return HttpResponseRedirect(r('cliente'))


def locacao_list(request):
    locacao = Locacao.objects.all()
    context = {'locacoes': locacao}
    return render(request, 'locacao/locacao_list.html', context)


def locacao_new(request):

    if request.method == 'GET':
        context = {'label': 'Cadastrar', 'form': LocacaoForm()}
        return render(request, 'locacao/locacao.html', context)

    form = LocacaoForm(request.POST)
    context = {'label': 'Cadastrar', 'form': form}

    if not form.is_valid():
        return render(request, 'locacao/locacao.html', context)

    Locacao.objects.create(**form.cleaned_data)

    msg = 'Cadastro realizado com sucesso!!'
    messages.success(request, msg)
    return HttpResponseRedirect(r('locacao'))


def locacao_edit(request, pk):
    locacao = get_object_or_404(Locacao, pk=pk)
    if request.method == "POST":
        try:
            form = LocacaoForm(request.POST, instance=locacao)
        except:
            raise
        if form.is_valid():
            locacao = form.save(commit=False)
            locacao.save()
            msg = 'Update realizado com sucesso!!'
            messages.success(request, msg)
            return HttpResponseRedirect(r('locacao'))
    else:
        form = LocacaoForm(instance=locacao)

    context = {'label': 'Editar', 'form': form}
    return render(request, 'locacao/locacao.html', context)


def devolucao_list(request):
    devolucoes = Devolucao.objects.all()
    context = {'devolucoes': devolucoes}
    return render(request, 'devolucao/devolucao_list.html', context)


def devolucao_new(request):

    if request.method == 'GET':
        context = {'label': 'Cadastrar', 'form': DevolucaoForm()}
        return render(request, 'devolucao/devolucao.html', context)

    form = DevolucaoForm(request.POST)
    context = {'label': 'Cadastrar', 'form': form}

    if not form.is_valid():
        return render(request, 'devolucao/devolucao.html', context)

    devolucao = Devolucao.objects.create(**form.cleaned_data)

    msg = 'Cadastro realizado com sucesso!!'
    messages.success(request, msg)

    # verificar se tem reserva para esse veiculo e enviar email para o cliente
    reserva = Reserva.objects.filter(veiculo=devolucao.locacao.veiculo, finalizada=False).order_by('-created_at')

    if reserva:
        # envia para o primeiro cliente a fazer a reserva
        _send_email('Reserva Disponível',
                    settings.DEFAULT_FROM_EMAIL,
                    devolucao.locacao.cliente.email,
                    'reserva/reserva_email.txt',
                    { 'reserva': reserva[0] }
                    )

    return HttpResponseRedirect(r('devolucao'))


def devolucao_edit(request, pk):
    devolucao = get_object_or_404(Devolucao, pk=pk)
    if request.method == "POST":
        try:
            form = DevolucaoForm(request.POST, instance=devolucao)
        except:
            raise
        if form.is_valid():
            devolucao = form.save(commit=False)
            devolucao.save()
            msg = 'Update realizado com sucesso!!'
            messages.success(request, msg)
            return HttpResponseRedirect(r('devolucao'))
    else:
        form = DevolucaoForm(instance=devolucao)

    context = {'label': 'Editar', 'form': form}

    return render(request, 'devolucao/devolucao.html', context)


def reserva_list(request):
    reservas = Reserva.objects.all()
    context = {'reservas': reservas}
    return render(request, 'reserva/reserva_list.html', context)


def reserva_new(request):
    if request.method == 'GET':
        context = {'label': 'Cadastrar', 'form': ReservaForm()}
        return render(request, 'reserva/reserva.html', context)

    form = ReservaForm(request.POST)
    context = {'label': 'Cadastrar', 'form': form}

    if not form.is_valid():
        return render(request, 'reserva/reserva.html', context)

    Reserva.objects.create(**form.cleaned_data)

    msg = 'Cadastro realizado com sucesso!!'
    messages.success(request, msg)
    return HttpResponseRedirect(r('reserva'))


def reserva_edit(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == "POST":
        try:
            form = ReservaForm(request.POST, instance=reserva)
        except:
            raise
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.save()
            msg = 'Update realizado com sucesso!!'
            messages.success(request, msg)
            return HttpResponseRedirect(r('reserva'))
    else:
        form = ReservaForm(instance=reserva)
    context = {'label': 'Editar', 'form': form}
    return render(request, 'reserva/reserva.html', context)



# login Desativado

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


def _send_email(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    send_email = MailSender(subject=subject,
                            body=body,
                            to=[to],
                            bcc=[from_],
                            from_email=from_)
    send_email.send()