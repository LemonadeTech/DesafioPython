from car_location.location.models import CategoriaVeiculo, Veiculo
from rest_framework import status
from django.shortcuts import resolve_url as r
from rest_framework.test import APITestCase


class VeiculoApiTests(APITestCase):

    def setUp(self):
        self.categoria = CategoriaVeiculo.objects.create(nome='Carro')
        self.data  = dict(modelo='Palio', categoria=self.categoria.pk, quilometragem=55)

    def test_new_veiculo(self):
        """
        Criando  veículo
        """

        url = r('location:veiculo-list')

        response = self.client.post(url, self.data, format='json')
        with self.subTest():
                self.assertEqual(response.status_code, status.HTTP_201_CREATED)
                self.assertEqual(Veiculo.objects.count(), 1)
                self.assertEqual(Veiculo.objects.get().modelo, 'Palio')
                self.assertEqual(Veiculo.objects.get().categoria, self.categoria)
                self.assertEqual(Veiculo.objects.get().quilometragem,  55)

    def test_detail_veiculo(self):
        '''
        detalhe do veículo
        '''

        self.obj = Veiculo.objects.create(
            modelo='Palio',
            categoria=self.categoria,
            quilometragem=55
        )

        url = r('location:veiculo-detail', self.obj.pk)

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_delete_categoria(self):
        """
        removendo veiculo

        """
        self.obj = Veiculo.objects.create(
            modelo='Palio',
            categoria=self.categoria,
            quilometragem=55
        )

        url = r('location:veiculo-detail', self.obj.pk)

        response = self.client.delete(url[1:])

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
