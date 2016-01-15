from car_location.location.serializers import CategoriaVeiculoViewSet
from rest_framework import routers
__author__ = 'lucas'


router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
router.register(r'categoriasveiculos', CategoriaVeiculoViewSet)
# router.register(r'veiculo', UserViewSet)
# urlpatterns = router.urls
