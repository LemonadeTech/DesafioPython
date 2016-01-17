import unittest
from car_location.location.models.categoriaveiculo import CategoriaVeiculo
from car_location.location.models.cliente import Cliente
from car_location.location.models.devolucao import Devolucao
from car_location.location.models.locacao import Locacao
from car_location.location.models.veiculo import Veiculo

__author__ = 'lucas'

from django.test import TestCase
from django.shortcuts import resolve_url as r


class DevolucaoNew(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('devolucao_new'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp,'devolucao/devolucao.html')
#
    def test_html(self):
        """HTML must contains input tags"""
        tags = (('<form',1),
                ('<input', 2),
                ('type="number"', 1),
                ('<select', 1),
                ('type="submit"',1))
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)
#
    def test_save_devolucao(self):
        cliente = Cliente.objects.create(nome='lucas', tipo_cnh='B', cpf='12345678901')
        categoria = CategoriaVeiculo.objects.create(nome='carro', tipo_cnh='B')
        veiculo = Veiculo.objects.create(modelo='Palio', quilometragem=10, disponivel=True, categoria=categoria)
        locacao = Locacao.objects.create(cliente=cliente, veiculo=veiculo,
                    data_inicial='2015-01-01',data_final='2015-01-10',
                    valor=20,devolvido=False)
        data = dict(locacao=locacao.pk, km_percorrido=10)
        resp = self.client.post(r('devolucao_new'), data)
        with self.subTest():
            self.assertTrue(Devolucao.objects.exists())
            self.assertTrue(Locacao.objects.get().devolvido)
            self.assertTrue(Veiculo.objects.get().disponivel)


class DevolucaoDetail(TestCase):
    def setUp(self):
        cliente = Cliente.objects.create(nome='lucas', tipo_cnh='B', cpf='12345678901')
        categoria = CategoriaVeiculo.objects.create(nome='carro', tipo_cnh='B')
        veiculo = Veiculo.objects.create(modelo='Palio', quilometragem=10, disponivel=True, categoria=categoria)
        locacao = Locacao.objects.create(cliente=cliente, veiculo=veiculo,
                    data_inicial='2015-01-01',data_final='2015-01-10',
                    valor=20,devolvido=False)

        self.data = dict(locacao=locacao, km_percorrido=10)
        self.obj = Devolucao.objects.create(**self.data)
        self.resp = self.client.get(r('devolucao_detail', self.obj.pk))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    @unittest.skip('implements')
    def test_edit_devolucao(self):
        pass


class DevolucaoList(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('devolucao'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp,'devolucao/devolucao_list.html')