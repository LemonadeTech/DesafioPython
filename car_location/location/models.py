from django.db import models


class CategoriaVeiculo(models.Model):
    nome = models.CharField('nome', max_length=50)

    class Meta:
        verbose_name_plural = 'categorias de veículos'
        verbose_name = 'categoria do veículo'

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    modelo = models.CharField('modelo', max_length=50)
    categoria = models.ForeignKey(CategoriaVeiculo, verbose_name='categoria')
    quilometragem = models.FloatField('quilometragem')

    class Meta:
        verbose_name_plural = 'veículos'
        verbose_name = 'veículo'

    def __str__(self):
        return self.modelo


class Cliente(models.Model):
    nome = models.CharField('nome', max_length=255)
    cpf= models.CharField('cpf', max_length=11, primary_key=True)
    tipo_cnh= models.CharField('tipo cnh', max_length=2)
    phone = models.CharField('telefone', max_length=20, null=True)
    email = models.EmailField('email', null=True)

    class Meta:
        verbose_name_plural = 'clientes'
        verbose_name = 'cliente'

    def __str__(self):
        return self.nome


class Locacao(models.Model):
    cliente = models.ForeignKey(Cliente, verbose_name='cliente')
    veiculo = models.ForeignKey(Veiculo, verbose_name='veiculo')
    data_inicial = models.DateField('data locacão')
    data_final = models.DateField('data devolução')
    km_inicial = models.FloatField('km inicial do veículo', null=False)
    km_final = models.FloatField('km final do veículo', null=True)
    valor = models.FloatField('valor', null=False)
    multa = models.FloatField('multa', default=0)

    class Meta:
        verbose_name_plural = 'locações'
        verbose_name = 'locação'

    def __str__(self):
        return self.cliente.cpf + ' ' + self.veiculo.modelo