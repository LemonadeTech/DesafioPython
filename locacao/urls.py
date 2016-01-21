from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^index', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
	
	url(r'^veiculos/$', views.listaVeiculos, name='veiculos'),
	url(r'^veiculos/cadastro/', views.cadastroVeiculo, name='cadastroVeiculo'),
	url(r'^clientes/$', views.listaClientes, name='clientes'),
	url(r'^clientes/cadastro/', views.cadastroCliente, name='cadastroCliente'),
	url(r'^locacao/$', views.listaLocacao, name='locacao'),
	url(r'^locacao/cadastro/', views.cadastroLocacao, name='cadastroLocacao'),
	
	
	url(r'^api/consultarVeiculos/$', views.veiculosList, name='consultarVeiculos'),
	url(r'^api/consultarVeiculos/(?P<pk>[0-9]+)/$', views.veiculosDetail, name='consultarVeiculos'),
	url(r'^api/consultarVeiculos/categoria/(?P<pk>[0-9]+)/$', views.veiculosListagem, name='consultarVeiculos'),
	
	url(r'^api/consultarClientes/$', views.clientesList, name='consultarClientes'),
	url(r'^api/consultarClientes/(?P<pk>[0-9]+)/$', views.clientesDetail, name='consultarClientes'),

	url(r'^api/consultarLocacao/$', views.locacaoList, name='consultarLocacao'),
	url(r'^api/consultarLocacao/(?P<pk>[0-9]+)/$', views.locacaoDetail, name='consultarLocacao'),
	
	url(r'^api/consultarIndex', views.consultarIndex, name='consultarIndex'),
]
