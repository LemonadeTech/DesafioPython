from car_location.location.models.categoriaveiculo import CategoriaVeiculo
from car_location.location.models.cliente import Cliente
from car_location.location.models.locacao import Locacao
from car_location.location.models.reserva import Reserva
from car_location.location.models.veiculo import Veiculo
from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r


class ReservaEmailTest(TestCase):
    def setUp(self):
        cliente = Cliente.objects.create(nome='lucas', tipo_cnh='B', cpf='12345678901', email='lffsantos@gmail.com')
        categoria = CategoriaVeiculo.objects.create(nome='carro', tipo_cnh='B')
        veiculo = Veiculo.objects.create(modelo='Palio', quilometragem=10, disponivel=True, categoria=categoria)
        locacao = Locacao.objects.create(cliente=cliente, veiculo=veiculo,
                    data_inicial='2015-01-01',data_final='2015-01-10',
                    valor=20,devolvido=False)
        self.obj = Reserva.objects.create(nome="reserva_1", veiculo=veiculo, cliente=cliente)
        data = dict(locacao=locacao.pk, km_percorrido=10)
        resp = self.client.post(r('devolucao_new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        
        expect = 'Reserva Disponível'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):

        expect = 'contato@rentcar.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['lffsantos@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_cco(self):
        expect = ['contato@rentcar.com.br']

        self.assertEqual(expect, self.email.bcc)


    def test_subscription_email_body(self):
        contents = ['reserva_1',
                    'Palio',
                    'Lucas']
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)