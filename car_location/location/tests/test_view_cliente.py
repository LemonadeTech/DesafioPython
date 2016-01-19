from car_location.location.models.cliente import Cliente

__author__ = 'lucas'

from django.test import TestCase
from django.shortcuts import resolve_url as r


class ClienteNew(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('cliente_new'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp,'cliente/clientes.html')

    def test_html(self):
        """HTML must contains input tags"""
        tags = (('<form',1),
                ('<input', 6),
                ('type="text"', 4),
                ('type="submit"',1))
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_save_cliente(self):
        self.data = dict(nome='lucas', tipo_cnh='B', cpf='12345678901')
        resp = self.client.post(r('cliente_new'), self.data)
        self.assertTrue(Cliente.objects.exists())


class ClienteDetail(TestCase):
    def setUp(self):
        self.data = dict(nome='lucas', tipo_cnh='B', cpf='12345678901')
        self.obj = Cliente.objects.create(**self.data)
        self.resp = self.client.get(r('cliente_detail', self.obj.pk))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_edit_cliente(self):

        self.assertEqual(Cliente.objects.get().nome, 'lucas')
        self.data['nome'] = 'joão'
        resp = self.client.post(r('cliente_detail', self.obj.pk), self.data)
        self.assertEqual(Cliente.objects.get().nome, 'joão')


class ClienteList(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('cliente'))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp,'cliente/clientes_list.html')