__author__ = 'lucas'
from car_location.location.models.categoriaveiculo import CategoriaVeiculo
from rest_framework import status
from django.shortcuts import resolve_url as r
from rest_framework.test import APITestCase


class CategoriaVeiculoApiTests(APITestCase):

    def test_new_categoria(self):
        """
        Criando categoria de veículo
        """
        url = r('location:categoriaveiculo-list')
        data = {'nome': 'Carro', 'tipo_cnh': 'B'}
        response = self.client.post(url, data, format='json')
        with self.subTest():
                self.assertEqual(response.status_code, status.HTTP_201_CREATED)
                self.assertEqual(CategoriaVeiculo.objects.count(), 1)
                self.assertEqual(CategoriaVeiculo.objects.get().nome, 'carro')

    def test_detail_categoria(self):
        '''
        detalhe de uma categoria
        '''

        self.obj = CategoriaVeiculo.objects.create(
            nome='Carro',
        )

        url = r('location:categoriaveiculo-detail', self.obj.pk)

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_categoria(self):
        self.obj = CategoriaVeiculo.objects.create(
            nome='Carro',
        )
        url = r('location:categoriaveiculo-detail', self.obj.pk)

        response = self.client.delete(url[1:])
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)