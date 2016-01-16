from datetime import datetime
from car_location.location.models.categoriaveiculo import CategoriaVeiculo
from car_location.location.models.cliente import Cliente
from car_location.location.models.devolucao import Devolucao
from car_location.location.models.locacao import Locacao
from car_location.location.models.veiculo import Veiculo
from rest_framework import status

__author__ = 'lucas'
from django.shortcuts import resolve_url as r
from rest_framework.test import APITestCase


class DevolucaoApiTests(APITestCase):
    def setUp(self):
        self.categoria = CategoriaVeiculo.objects.create(nome='Carro', tipo_cnh='B,C')
        self.veiculo = Veiculo.objects.create(modelo='Palio',
                                         categoria=self.categoria,
                                         quilometragem=55,
                                         disponivel=False)

        self.cliente = Cliente.objects.create(nome='lucas', cpf='12345678901',
                                         tipo_cnh='B', email='lucas@test.com',
                                         phone='719991625771')

        self.locacao = Locacao.objects.create(cliente=self.cliente,
                                              veiculo=self.veiculo,
                    data_inicial='2015-01-23', data_final='2015-01-27',
                    km_inicial=self.veiculo.quilometragem, valor=10)

        self.data  = dict(locacao=self.locacao.pk, km_percorrido=10)

    def test_new_Devolucao(self):
        """
        cadastrando devolução
        """

        url = r('location:devolucao-list')
        response = self.client.post(url, self.data, format='json')
        with self.subTest():
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(Devolucao.objects.count(), 1)
            self.assertEqual(Locacao.objects.get().devolvido, True)
            self.assertIsInstance(Devolucao.objects.get().data_entrega, datetime)
            self.assertEqual(Veiculo.objects.get().disponivel, True)

    def test_detail_devolucao(self):
        '''
        detalhe da devolucao
        '''

        self.obj = Devolucao.objects.create(locacao=self.locacao, km_percorrido=10)

        url = r('location:devolucao-detail', self.obj.pk)

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_delete_devolucao(self):
        """
        removendo devolução

        """
        self.obj = Devolucao.objects.create(locacao=self.locacao, km_percorrido=10)

        url = r('location:devolucao-detail', self.obj.pk)

        response = self.client.delete(url[1:])

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

