from car_location.location.models.cliente import Cliente
from car_location.location.models.veiculo import Veiculo
from django.db import models
from rest_framework import serializers

__author__ = 'lucas'


class Locacao(models.Model):
    cliente = models.ForeignKey(Cliente, verbose_name='cliente')
    veiculo = models.ForeignKey(Veiculo, verbose_name='veiculo')
    data_inicial = models.DateField('data locacão')
    data_final = models.DateField('data de devolução')
    data_entrega = models.DateField('data da entrega', null=True)
    km_inicial = models.FloatField('km inicial do veículo', null=False)
    km_final = models.FloatField('km final do veículo', null=True)
    valor = models.FloatField('valor', null=False)
    multa = models.FloatField('multa', default=0)

    class Meta:
        verbose_name_plural = 'locações'
        verbose_name = 'locação'

    def __str__(self):
        return self.cliente.cpf + ' ' + self.veiculo.modelo


class LocacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locacao
