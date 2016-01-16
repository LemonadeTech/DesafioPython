from car_location.location.models import CategoriaVeiculo, Veiculo, Cliente, \
    Locacao
from rest_framework import serializers, viewsets

__author__ = 'lucas'


class CategoriaVeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaVeiculo


class CategoriaVeiculoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaVeiculo.objects.all()
    serializer_class = CategoriaVeiculoSerializer


class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo


class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class LocacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locacao


class LocacaoViewSet(viewsets.ModelViewSet):
    queryset = Locacao.objects.all()
    serializer_class = LocacaoSerializer