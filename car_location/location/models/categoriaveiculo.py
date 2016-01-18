import json
from django.db import models
from rest_framework import serializers

__author__ = 'lucas'


class CategoriaVeiculo(models.Model):
    nome = models.CharField('nome', max_length=50, unique=True)
    tipo_cnh = models.CharField(max_length=20)

    def settipo_cnh(self, cnh):
        self.tipo_cnh = json.dumps(cnh)

    def gettipo_cnh(self, x):
        return json.loads(self.tipo_cnh)

    def save(self, *args, **kwargs):
        self.nome = self.nome.lower()
        super(CategoriaVeiculo, self).save(*args, **kwargs)  # Call the "real" save() method.

    class Meta:
        verbose_name_plural = 'categorias de veículos'
        verbose_name = 'categoria do veículo'

    def __str__(self):
        return self.nome


class CategoriaVeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaVeiculo