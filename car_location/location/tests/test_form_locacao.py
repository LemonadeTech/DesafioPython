from car_location.location.forms import LocacaoForm
from car_location.location.models.categoriaveiculo import CategoriaVeiculo
from car_location.location.models.cliente import Cliente
from car_location.location.models.veiculo import Veiculo

__author__ = 'lucas'

from django.test import TestCase


class LocacaoFormTest(TestCase):

    def test_form_has_fields(self):
        form = LocacaoForm()
        fields = ['cliente', 'veiculo','data_inicial', 'data_final',
                  'km_inicial', 'valor', 'devolvido']
        self.assertSequenceEqual(fields,list(form.fields))

    def test_form_save_invalid_datas_iguais(self):
        form = self.make_validated_form(data_inicial='2015-01-20', data_final='2015-01-20')
        self.assertEqual(form.errors.as_data()['__all__'][0].messages[0], 'O período de locação deve ser maior do que 1 dia')

    def test_form_save_invalid_data_inicial_maior(self):
        form = self.make_validated_form(data_inicial='2015-01-25', data_final='2015-01-20')
        self.assertEqual(form.errors.as_data()['__all__'][0].messages[0], 'A data de entrega não pode ser menor do que a data de locação')

    def make_validated_form(self, **kwargs):
        cliente = Cliente.objects.create(nome='lucas', tipo_cnh='B', cpf='12345678901')
        categoria = CategoriaVeiculo.objects.create(nome='carro', tipo_cnh='B')
        veiculo = Veiculo.objects.create(modelo='Palio', quilometragem=10, disponivel=True, categoria=categoria)

        data = dict(cliente=cliente.pk, veiculo=veiculo.pk,
                    data_inicial='2015-01-15',data_final='2015-01-20',
                    valor=20,devolvido=False)

        valid = dict(data)
        data = dict(valid, **kwargs)
        form = LocacaoForm(data)
        form.is_valid()
        return form
