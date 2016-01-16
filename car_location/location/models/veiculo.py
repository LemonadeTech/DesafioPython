from car_location.location.models.categoriaveiculo import CategoriaVeiculo
from django.db import models
from rest_framework import serializers

__author__ = 'lucas'

class Veiculo(models.Model):
    modelo = models.CharField('modelo', max_length=50)
    categoria = models.ForeignKey(CategoriaVeiculo, verbose_name='categoria')
    quilometragem = models.FloatField('quilometragem')

    class Meta:
        verbose_name_plural = 'veículos'
        verbose_name = 'veículo'

    def __str__(self):
        return self.modelo


class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo



