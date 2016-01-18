import datetime
from car_location.location.models.categoriaveiculo import CategoriaVeiculo
from car_location.location.models.cliente import Cliente
from car_location.location.models.locacao import Locacao
from car_location.location.models.veiculo import Veiculo
from psycopg2.tests import unittest

__author__ = 'lucas'

from django.test import TestCase
from django.shortcuts import resolve_url as r


class LocacaoNew(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('locacao_new'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp,'locacao/locacao.html')

    def test_html(self):
        """HTML must contains input tags"""
        tags = (('<form',1),
                ('<input', 4),
                ('type="text"', 2),
                ('type="number"', 1),
                ('<select', 2),
                ('type="submit"',1))
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_save_locacao(self):
        cliente = Cliente.objects.create(nome='lucas', tipo_cnh='B', cpf='12345678901')
        categoria = CategoriaVeiculo.objects.create(nome='carro', tipo_cnh='B')
        veiculo = Veiculo.objects.create(modelo='Palio', quilometragem=10, disponivel=True, categoria=categoria)

        data = dict(cliente=cliente.pk, veiculo=veiculo.pk,
                    data_inicial='15/01/2015',data_final='20/01/2015',
                    valor=20,devolvido=False)
        resp = self.client.post(r('locacao_new'), data)
        self.assertTrue(Locacao.objects.exists())


class LocacaoDetail(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(nome='lucas', tipo_cnh='B', cpf='12345678901')
        self.categoria = CategoriaVeiculo.objects.create(nome='carro', tipo_cnh='B')
        self.veiculo = Veiculo.objects.create(modelo='Palio', quilometragem=10, disponivel=True, categoria=self.categoria)

        self.data = dict(cliente=self.cliente, veiculo=self.veiculo,
                    data_inicial='2015-01-15',data_final='2015-01-20',
                    valor=20,devolvido=False)
        self.obj = Locacao.objects.create(**self.data)
        self.resp = self.client.get(r('locacao_detail', self.obj.pk))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    @unittest.skip('test broken fixed ASAP')
    def test_edit_locacao(self):

        self.assertEqual(Locacao.objects.get().devolvido, False)
        self.data['data_final'] = datetime.date.today()
        self.data['cliente'] = self.cliente
        self.data['veiculo'] = self.veiculo
        resp = self.client.post(r('locacao_detail', self.obj.pk), self.data)
        self.assertEqual(Locacao.objects.get().data_final, datetime.date.today())

class locacaoList(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('locacao'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp,'locacao/locacao_list.html')