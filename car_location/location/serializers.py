from car_location.location.models import CategoriaVeiculo
from rest_framework import serializers, viewsets

__author__ = 'lucas'


class CategoriaVeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaVeiculo


class CategoriaVeiculoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaVeiculo.objects.all()
    serializer_class = CategoriaVeiculoSerializer

