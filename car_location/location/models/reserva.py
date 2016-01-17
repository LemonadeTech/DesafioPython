from car_location.location.models.cliente import Cliente
from car_location.location.models.veiculo import Veiculo
from django.db import models

__author__ = 'lucas'


class Reserva(models.Model):
    nome = models.CharField('nome da reserva', max_length=100)
    veiculo = models.ForeignKey(Veiculo, verbose_name='veículo')
    cliente = models.ForeignKey(Cliente, verbose_name='cliente')
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    finalizada = models.BooleanField('finalizada', default=False)

    class Meta:
        verbose_name_plural = 'reservas'
        verbose_name = 'reserva'

    def __str__(self):
        return self.nome