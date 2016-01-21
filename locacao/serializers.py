from locacao.models import Veiculos, Clientes, Devolucao
from rest_framework import serializers

class VeiculosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculos
        fields = ('id', 'tipo_carro', 'placa', 'modelo', 'categoria', 'quilometragem')

class ClientesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Clientes
		fields = ('id', 'nome_cliente', 'CPF_cliente', 'CNH_cliente', 'telefone_cliente', 'email_cliente')
		
class DevolucaoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Devolucao
		fields = ('id', 'id_cliente', 'id_veiculos', 'quilometragem_inicial','quilometragem_final', 'data_locacao', 'data_devolucao')
