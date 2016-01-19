from car_location.location.models.locacao import Locacao
from django.db import models
from rest_framework import serializers

__author__ = 'lucas'


class Devolucao(models.Model):
    locacao = models.OneToOneField(Locacao, verbose_name='locação', unique=True)
    km_percorrido = models.FloatField('km percorrido', null=True)
    data_entrega = models.DateTimeField('data da entrega', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'devoluções'
        verbose_name = 'devolução'

    def __str__(self):
        return self.locacao

    def save(self, *args, **kwargs):
        self.locacao.devolvido = True
        self.locacao.veiculo.quilometragem += self.km_percorrido
        self.locacao.veiculo.save()
        self.locacao.save()
        super(Devolucao, self).save(*args, **kwargs)  # Call the "real" save() method.




class DevolucaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devolucao

