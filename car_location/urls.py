from car_location.location.views import home, do_login, do_logout, categoria, \
    veiculo, cliente, locacao, devolucao, categoria_new, categoria_detail
from django.conf.urls import url, include

from car_location.location.routers import router
from django.contrib import admin

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^categoria/$', categoria, name='categoria'),
    url(r'^categoria/new/$', categoria_new, name='categoria_new'),
    url(r'^categoria/detalhe/(\d+)/$', categoria_detail, name='categoria_detail'),
    url(r'^veiculo/', veiculo, name='veiculo'),
    url(r'^cliente/', cliente, name='cliente'),
    url(r'^locacao/', locacao, name='locacao'),
    url(r'^devolucao/', devolucao, name='devolucao'),
    url(r'^login/$', do_login, name='login'),
    url(r'^logout/$', do_logout, name='logout'),
    url(r'^api/v1/', include(router.urls, namespace='location')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),

]