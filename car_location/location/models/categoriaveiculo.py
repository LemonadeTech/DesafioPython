from django.db import models
from rest_framework import serializers

__author__ = 'lucas'


class CategoriaVeiculo(models.Model):
    nome = models.CharField('nome', max_length=50)

    class Meta:
        verbose_name_plural = 'categorias de veículos'
        verbose_name = 'categoria do veículo'

    def __str__(self):
        return self.nome


class CategoriaVeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaVeiculo