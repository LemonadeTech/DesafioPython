from django.conf.urls import url, include

from car_location.location.routers import router
from django.contrib import admin

urlpatterns = [
    url(r'^api/v1/', include(router.urls, namespace='location')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
]