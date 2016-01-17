from car_location.location.views import home, do_login, do_logout, \
    categoria_new, categoria_edit, \
    veiculo_edit, veiculo_new, categoria_list, veiculo_list, cliente_list, \
    cliente_new, cliente_edit, locacao_list, locacao_new, locacao_edit, \
    devolucao_list, devolucao_new, devolucao_edit, reserva_list, reserva_new, \
    reserva_edit
from django.conf.urls import url, include

from car_location.location.routers import router
from django.contrib import admin

urlpatterns = [
    url(r'^$', home, name='home'),

    url(r'^categoria/$', categoria_list, name='categoria'),
    url(r'^categoria/new/$', categoria_new, name='categoria_new'),
    url(r'^categoria/detalhe/(\d+)/$', categoria_edit, name='categoria_detail'),

    url(r'^veiculo/$', veiculo_list, name='veiculo'),
    url(r'^veiculo/new/$', veiculo_new, name='veiculo_new'),
    url(r'^veiculo/detalhe/(\d+)/$', veiculo_edit, name='veiculo_detail'),

    url(r'^cliente/$', cliente_list, name='cliente'),
    url(r'^cliente/new/$', cliente_new, name='cliente_new'),
    url(r'^cliente/detalhe/(\d+)/$', cliente_edit, name='cliente_detail'),

    url(r'^locacao/$', locacao_list, name='locacao'),
    url(r'^locacao/new/$', locacao_new, name='locacao_new'),
    url(r'^locacao/detalhe/(\d+)/$', locacao_edit, name='locacao_detail'),

    url(r'^devolucao/$', devolucao_list, name='devolucao'),
    url(r'^devolucao/new/$', devolucao_new, name='devolucao_new'),
    url(r'^devolucao/detalhe/(\d+)/$', devolucao_edit, name='devolucao_detail'),

    url(r'^reserva/$', reserva_list, name='reserva'),
    url(r'^reserva/new/$', reserva_new, name='reserva_new'),
    url(r'^reserva/detalhe/(\d+)/$', reserva_edit, name='reserva_detail'),

    url(r'^login/$', do_login, name='login'),
    url(r'^logout/$', do_logout, name='logout'),
    url(r'^api/v1/', include(router.urls, namespace='location')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),

]