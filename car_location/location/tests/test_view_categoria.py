from car_location.location.models.categoriaveiculo import CategoriaVeiculo

__author__ = 'lucas'

from django.test import TestCase
from django.shortcuts import resolve_url as r


class CategoriaVeiculosNew(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('categoria_new'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp,'categoria_veiculo/categoria_veiculos.html')

    def test_html(self):
        """HTML must contains input tags"""
        tags = (('<form',1),
                ('<input', 3),
                ('type="text"', 2),
                ('type="submit"',1))
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_save_categoria(self):
        data = dict(nome='carro', tipo_cnh='A,B')
        resp = self.client.post(r('categoria_new'), data)
        self.assertTrue(CategoriaVeiculo.objects.exists())


class CategoriaVeiculosDetail(TestCase):
    def setUp(self):
        self.data = dict(nome='carro', tipo_cnh='A,B')
        self.obj = CategoriaVeiculo.objects.create(**self.data)
        self.resp = self.client.get(r('categoria_detail', self.obj.pk))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_edit_categoria(self):

        self.assertEqual(CategoriaVeiculo.objects.get().nome, 'carro')
        self.data['nome'] = 'moto'
        resp = self.client.post(r('categoria_detail', self.obj.pk), self.data)
        self.assertEqual(CategoriaVeiculo.objects.get().nome, 'moto')


class CategoriaVeiculosList(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('categoria'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp,'categoria_veiculo/categoria_veiculos_list.html')