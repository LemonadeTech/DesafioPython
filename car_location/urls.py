from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from car_location.location.routers import router

urlpatterns = [
    url(r'^api/v1/', include(router.urls, namespace='location')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]