from car_location.location.models.categoriaveiculo import CategoriaVeiculo, \
    CategoriaVeiculoSerializer
from car_location.location.models.cliente import Cliente
from car_location.location.models.cliente import ClienteSerializer
from car_location.location.models.devolucao import Devolucao, \
    DevolucaoSerializer
from car_location.location.models.locacao import Locacao, LocacaoSerializer
from car_location.location.models.veiculo import Veiculo
from car_location.location.models.veiculo import VeiculoSerializer
from rest_framework import viewsets

__author__ = 'lucas'


class CategoriaVeiculoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaVeiculo.objects.all()
    serializer_class = CategoriaVeiculoSerializer


class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer



class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class LocacaoViewSet(viewsets.ModelViewSet):
    queryset = Locacao.objects.all()
    serializer_class = LocacaoSerializer


class DevolucaoViewSet(viewsets.ModelViewSet):
    queryset = Devolucao.objects.all()
    serializer_class = DevolucaoSerializer

