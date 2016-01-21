from datetime import date
from django.db import models

class Veiculos(models.Model):
	id      		=   models.AutoField(primary_key=True)
	tipo_carro 		=	models.CharField(max_length=10)
	placa 			=	models.CharField(max_length=8)
	modelo 			= 	models.CharField(max_length=50)
	categoria 		= 	models.CharField(max_length=20)
	quilometragem 	= 	models.IntegerField()
	disponivel		= 	models.BooleanField(default=True)

	def __unicode__(self):
		return self.placa

class Clientes(models.Model):
	id      			= models.AutoField(primary_key=True)
	nome_cliente 		= models.CharField(max_length=200)
	CPF_cliente 		= models.CharField(max_length=11)
	CNH_cliente 		= models.CharField(max_length=20)
	telefone_cliente 	= models.CharField(max_length=12)
	email_cliente 		= models.EmailField()

	def __unicode__(self):
		return self.nome_cliente
		
class Devolucao(models.Model):
	id						=	models.AutoField(primary_key=True)
	id_cliente				=	models.ForeignKey(Clientes, on_delete = models.CASCADE)
	id_veiculos				=	models.ForeignKey(Veiculos, on_delete = models.CASCADE)
	quilometragem_inicial	=	models.IntegerField(default=0)
	quilometragem_final		=	models.IntegerField(default=0)
	data_locacao			=	models.CharField(max_length=10)
	data_devolucao			=	models.CharField(max_length=10)

	def __unicode__(self):
		return self.id