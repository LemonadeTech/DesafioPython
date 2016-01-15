from car_location.location.serializers import CategoriaVeiculoViewSet, \
    VeiculoViewSet
from rest_framework import routers
__author__ = 'lucas'


router = routers.DefaultRouter()
router.register(r'categoriasveiculos', CategoriaVeiculoViewSet)
router.register(r'veiculos', VeiculoViewSet)
