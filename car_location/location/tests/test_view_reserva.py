from car_location.location.models.categoriaveiculo import CategoriaVeiculo
from car_location.location.models.cliente import Cliente
from car_location.location.models.reserva import Reserva
from car_location.location.models.veiculo import Veiculo

__author__ = 'lucas'

from django.test import TestCase
from django.shortcuts import resolve_url as r


class ReservaNew(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('reserva_new'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp,'reserva/reserva.html')

    def test_html(self):
        """HTML must contains input tags"""
        tags = (('<form',1),
                ('<input', 3),
                ('<select', 2),
                ('type="submit"',1))
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_save_reserva(self):
        self.categoria = CategoriaVeiculo.objects.create(nome='carro', tipo_cnh='B')
        self.cliente = Cliente.objects.create(nome='lucas', tipo_cnh='B', cpf='12345678901')
        self.veiculo = Veiculo.objects.create(modelo='Palio', quilometragem=10, disponivel=False, categoria=self.categoria)
        self.data = dict(nome="reserva_1", veiculo=self.veiculo.pk, cliente=self.cliente.pk, finalizada=False)
        resp = self.client.post(r('reserva_new'), self.data)
        self.assertTrue(Reserva.objects.exists())


class ReservaDetail(TestCase):
    def setUp(self):
        self.categoria = CategoriaVeiculo.objects.create(nome='carro', tipo_cnh='B')
        self.cliente = Cliente.objects.create(nome='lucas', tipo_cnh='B', cpf='12345678901')
        self.veiculo = Veiculo.objects.create(modelo='Palio', quilometragem=10, disponivel=False, categoria=self.categoria)
        self.data = dict(nome="reserva_1", veiculo=self.veiculo, cliente=self.cliente)
        self.obj = Reserva.objects.create(**self.data)
        self.resp = self.client.get(r('reserva_detail', self.obj.pk))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)
#
    def test_edit_reserva(self):

        self.assertFalse(Reserva.objects.get().finalizada)
        self.data['finalizada'] = True
        self.data['cliente'] = self.cliente.pk
        self.data['veiculo'] = self.veiculo.pk
        resp = self.client.post(r('reserva_detail', self.obj.pk), self.data)
        self.assertTrue(Reserva.objects.get().finalizada)


class ReservaList(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('reserva'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp,'reserva/reserva_list.html')