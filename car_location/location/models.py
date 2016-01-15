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


# class Locacao(models.Model):
#     pass
#
#
# class Cliente(models.Model):
#     pass


