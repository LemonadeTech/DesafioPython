from car_location.location.models.categoriaveiculo import CategoriaVeiculo
from car_location.location.models.veiculo import Veiculo

__author__ = 'lucas'

from django.test import TestCase
from django.shortcuts import resolve_url as r


class VeiculosNew(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('veiculo_new'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp,'veiculo/veiculos.html')

    def test_html(self):
        """HTML must contains input tags"""
        tags = (('<form',1),
                ('<input', 4),
                ('type="text"', 1),
                ('type="number"', 1),
                ('type="checkbox"', 1),
                ('type="submit"',1))
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_save_veiculo(self):
        categoria = CategoriaVeiculo.objects.create(nome='carro', tipo_cnh='B')
        data = dict(modelo='Palio', quilometragem=10, disponivel=True, categoria=categoria)
        resp = self.client.post(r('veiculo_new'), data)
        self.assertTrue(CategoriaVeiculo.objects.exists())


class VeiculosDetail(TestCase):
    def setUp(self):
        self.categoria = CategoriaVeiculo.objects.create(nome='carro', tipo_cnh='B')
        self.data = dict(modelo='Palio', quilometragem=10, disponivel=True, categoria=self.categoria)
        self.obj = Veiculo.objects.create(**self.data)
        self.resp = self.client.get(r('veiculo_detail', self.obj.pk))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_edit_veiculo(self):

        self.assertEqual(Veiculo.objects.get().modelo, 'Palio')
        self.data['modelo'] = 'mudeionome'
        self.data['categoria'] = self.categoria.pk
        resp = self.client.post(r('veiculo_detail', self.obj.pk), self.data)
        self.assertEqual(Veiculo.objects.get().modelo, 'mudeionome')


class CategoriaVeiculosList(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('veiculo'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp,'veiculo/veiculos_list.html')