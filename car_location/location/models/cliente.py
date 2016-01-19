import json
from car_location.location.validators import validate_cpf
from django.db import models
from rest_framework import serializers

__author__ = 'lucas'


class Cliente(models.Model):
    nome = models.CharField('nome', max_length=255)
    cpf= models.CharField('cpf', max_length=11, unique=True, validators=[validate_cpf])
    tipo_cnh= models.CharField('tipo_cnh', max_length=20)
    phone = models.CharField('telefone', max_length=20, blank=True, default='')
    email = models.EmailField('email', blank=True, default='')

    class Meta:
        verbose_name_plural = 'clientes'
        verbose_name = 'cliente'

    def __str__(self):
        return self.nome


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
