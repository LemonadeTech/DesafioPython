from django.shortcuts 				import render
from locacao.models 				import Veiculos, Clientes, Devolucao
from django.http 					import HttpResponse, Http404, QueryDict
from rest_framework.decorators 		import api_view
from django.views.decorators.csrf 	import csrf_exempt
from rest_framework.response 		import Response
from locacao.serializers 			import VeiculosSerializer, ClientesSerializer, DevolucaoSerializer
from itertools import chain

def index(request):
	context = {}
	return render(request, 'index.html', context)

def listaVeiculos(request):
	context = {'titulo':"Veiculos", 'consultaURL':'consultarVeiculos'}	
	listaTabela = {"Tipo de Carro", "Placa", "Modelo","Categoria","Quilometragem"}
	context['listaTabela'] = listaTabela
	return render(request, 'tabela.html', context)

def cadastroVeiculo(request):
	context = {'titulo':"Veiculos", 'consultaURL':'consultarVeiculos','listaURL':'veiculos','formHTML':"formVeiculo.html"}
	return render(request, 'form_cadastro.html', context)
	
def listaClientes(request):
	context = {'titulo':"Clientes", 'consultaURL':'consultarClientes'}
	listaTabela = {"Nome", "CPF", "CNH","Telefone","E-Mail"}
	context['listaTabela'] = listaTabela
	return render(request, 'tabela.html', context)

def cadastroCliente(request):
	context = {'titulo':"Clientes", 'consultaURL':'consultarClientes','listaURL':'clientes','formHTML':"formCliente.html"}
	listaTabela = {"Cliente":"str", "CPF":"cpf", "CNH":"cnh","Telefone":"tele","E-Mail":"email"}
	context['listaTabela'] = listaTabela
	return render(request, 'form_cadastro.html', context)	

def listaLocacao(request):
	context = {'titulo':"Locação", 'consultaURL':'consultarLocacao'}	
	listaTabela = {"Cliente", "Placa do Carro","Quilometragem Inicial", "Data da Locação", "Data da Devolução"}
	context['listaTabela'] = listaTabela
	return render(request, 'tabela.html', context)
	
def cadastroLocacao(request):
	context = {'titulo':"Locação", 'consultaURL':'consultarLocacao','listaURL':'locacao','formHTML':"formLocacao.html"}	
	listaTabela = {"Cliente":"listaCliente","Carro": "ListaCarro"}
	context['listaTabela'] = listaTabela
	return render(request, 'form_cadastro.html', context)

@csrf_exempt
@api_view(['GET', 'POST'])
def veiculosList(request):
	#Lista todos os veiculos ou cria um novo veiculo
	if request.method == 'GET':
		veiculo = Veiculos.objects.all()
		serializer = VeiculosSerializer(veiculo, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = VeiculosSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		
@csrf_exempt		
@api_view(['GET', 'PUT', 'DELETE'])
def veiculosDetail(request, pk):
	#Retorna, atualiza ou deleta uma instancia de snippet.
	try:
		veiculo = Veiculos.objects.get(id=pk)
	except Veiculos.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
		
	if request.method == 'GET':
		serializer = VeiculosSerializer(veiculo)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = VeiculosSerializer(veiculo, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		veiculo.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super(MyView, self).dispatch(request, *args, **kwargs)

@api_view(['GET'])
def veiculosListagem(request,pk, format=None):
		cliente = Clientes.objects.get(id=pk)
		valor = cliente.CNH_cliente
		splitpk = valor.split(",")
		veiculos = []
		for cat in splitpk:
			veiculos = list(chain(veiculos,Veiculos.objects.filter(categoria__contains=cat)))
		serializer = VeiculosSerializer(veiculos, many=True)
		return Response(serializer.data)

@api_view(['GET', 'POST'])
def clientesList(request, format=None):
	#Lista todos os clientes ou cria um novo cliente
	if request.method == 'GET':
		cliente = Clientes.objects.all()
		serializer = ClientesSerializer(cliente, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = ClientesSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)		

@api_view(['GET', 'PUT', 'DELETE'])
def clientesDetail(request, pk):
	try:
		cliente = Clientes.objects.get(id=pk)
	except Clientes.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
		
	if request.method == 'GET':
		serializer = ClientesSerializer(cliente)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = ClientesSerializer(cliente, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		cliente.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

		
@api_view(['GET', 'POST'])
def locacaoList(request, format=None):
	#Lista todas as locações ou cria uma nova locação
	if request.method == 'GET':
		devolucao = Devolucao.objects.all()
		serializer = DevolucaoSerializer(devolucao, many=True)
		return Response(serializer.data)
		
	elif request.method == 'POST':
		qdict = QueryDict('',mutable=True)
		qdict.update(request.data)
		veiculo = Veiculos.objects.get(id=request.data['id_veiculos'])
		qdict['quilometragem_inicial'] = veiculo.quilometragem
		qdict['quilometragem_final'] = '0'
		qdict['data_devolucao'] = ''
		serializer = DevolucaoSerializer(data=qdict)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)		

@api_view(['GET', 'PUT', 'DELETE'])
def locacaoDetail(request, pk):
	try:
		locacao = Devolucao.objects.get(id=pk)
	except Devolucao.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
		
	if request.method == 'GET':
		serializer = DevolucaoSerializer(locacao)
		return Response(serializer.data)

	elif request.method == 'PUT':
		serializer = DevolucaoSerializer(locacao, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		Devolucao.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

		
		
@api_view(['GET'])
def consultarIndex(request):
	if request.method == "GET":
		result = {}
		result['veiculos']	= Veiculos.objects.count()
		result['clientes']	= Clientes.objects.count()
		result['locacao']	= Devolucao.objects.count()
		return Response(result)
		