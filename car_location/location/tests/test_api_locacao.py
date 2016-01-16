from django.utils.timezone import now

__author__ = 'lucas'
from car_location.location.models import CategoriaVeiculo, Veiculo, Locacao, \
    Cliente
from rest_framework import status
from django.shortcuts import resolve_url as r
from rest_framework.test import APITestCase


class LocacaoApiTests(APITestCase):

    def setUp(self):
        self.categoria = CategoriaVeiculo.objects.create(nome='Carro')
        self.veiculo = Veiculo.objects.create(modelo='Palio',
                                         categoria=self.categoria,
                                         quilometragem=55)
        self.cliente = Cliente.objects.create(nome='lucas', cpf='12345678901',
                                         tipo_cnh='A', email='lucas@test.com',
                                         phone='719991625771')

        self.data = dict(cliente=self.cliente.pk, veiculo=self.veiculo.pk,
                    data_inicial='2015-01-23', data_final='2015-01-27',
                    km_inicial=self.veiculo.quilometragem, valor=10)


    def test_new_locacao(self):
        """
        Nova locação
        """
        url = r('location:locacao-list')

        response = self.client.post(url, self.data, format='json')
        with self.subTest():
                self.assertEqual(response.status_code, status.HTTP_201_CREATED)
                self.assertEqual(Locacao.objects.count(), 1)


    def test_detail_locacao(self):
        '''
        detalhe da locação
        '''
        self.muda_atributos_data(cliente=self.cliente, veiculo=self.veiculo)

        self.obj = Locacao.objects.create(**self.data)

        url = r('location:locacao-detail', self.obj.pk)

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_locacao(self):
        """
        removendo locação

        """
        self.muda_atributos_data(cliente=self.cliente, veiculo=self.veiculo)

        self.obj = Locacao.objects.create(**self.data)

        url = r('location:locacao-detail', self.obj.pk)

        response = self.client.delete(url[1:])

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def muda_atributos_data(self, **kwargs):
        self.data = dict(self.data, **kwargs)