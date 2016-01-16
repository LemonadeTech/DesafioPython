from car_location.location.serializers import CategoriaVeiculoViewSet, \
    VeiculoViewSet, ClienteViewSet, LocacaoViewSet
from rest_framework import routers
__author__ = 'lucas'


router = routers.DefaultRouter()
router.register(r'categoriasveiculos', CategoriaVeiculoViewSet)
router.register(r'veiculos', VeiculoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'locacoes', LocacaoViewSet)
