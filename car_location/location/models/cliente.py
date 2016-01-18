import json
from django.db import models
from rest_framework import serializers

__author__ = 'lucas'


class Cliente(models.Model):
    nome = models.CharField('nome', max_length=255)
    cpf= models.CharField('cpf', max_length=11, unique=True)
    tipo_cnh= models.CharField('tipo_cnh', max_length=20)
    phone = models.CharField('telefone', max_length=20, null=True)
    email = models.EmailField('email', null=True)

    def settipo_cnh(self, cnh):
        self.tipo_cnh = json.dumps(cnh)

    def gettipo_cnh(self, x):
        return json.loads(self.tipo_cnh)

    class Meta:
        verbose_name_plural = 'clientes'
        verbose_name = 'cliente'

    def __str__(self):
        return self.nome


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
