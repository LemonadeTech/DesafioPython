__author__ = 'lucas'
from car_location.location.models import Cliente
from rest_framework import status
from django.shortcuts import resolve_url as r
from rest_framework.test import APITestCase


class ClienteApiTests(APITestCase):

    def setUp(self):
        self.data = dict(nome='lucas', cpf='12345678901', tipo_cnh='A', email='lucas@test.com', phone='719991625771')

    def test_new_cliente(self):
        """
        cadastro cliente
        """
        url = r('location:cliente-list')

        response = self.client.post(url, self.data, format='json')
        with self.subTest():
                self.assertEqual(response.status_code, status.HTTP_201_CREATED)
                self.assertEqual(Cliente.objects.count(), 1)
                self.assertEqual(Cliente.objects.get().nome, 'lucas')
                self.assertEqual(Cliente.objects.get().cpf, '12345678901')
                self.assertEqual(Cliente.objects.get().tipo_cnh,  'A')

    def test_detail_cliente(self):
        '''
        detalhe do cliente
        '''

        self.obj = Cliente.objects.create(**self.data)

        url = r('location:cliente-detail', self.obj.pk)

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_delete_cliente(self):
        """
        removendo cliente

        """
        self.obj = Cliente.objects.create(**self.data)

        url = r('location:cliente-detail', self.obj.pk)

        response = self.client.delete(url[1:])

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_campo_obrigatorio_cliente(self):
        self.muda_atributos_data(nome='', cpf='', tipo_cnh='')
        self.obj = Cliente.objects.create(**self.data)
        url = r('location:cliente-list')
        response = self.client.post(url, self.data, format='json')
        with self.subTest():
            self.assertEqual(response.data['nome'][0], 'Este campo não pode ser em branco.')
            self.assertEqual(response.data['cpf'][0], 'Este campo não pode ser em branco.')
            self.assertEqual(response.data['tipo_cnh'][0], 'Este campo não pode ser em branco.')
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def muda_atributos_data(self, **kwargs):
        self.data = dict(self.data, **kwargs)