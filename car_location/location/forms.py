from car_location.location.models.categoriaveiculo import CategoriaVeiculo
from car_location.location.models.cliente import Cliente
from car_location.location.models.veiculo import Veiculo
from django import forms

__author__ = 'lucas'

class CategoriaVeiculoForm(forms.ModelForm):

    class Meta:
        model = CategoriaVeiculo
        fields = ('nome', 'tipo_cnh',)


class VeiculoForm(forms.ModelForm):

    class Meta:
        model = Veiculo
        fields = ('modelo', 'categoria','quilometragem', 'disponivel')



class ClienteForm(forms.ModelForm):
    email = forms.EmailField(label="Email", required=False)
    phone = forms.CharField(label="Telefone", required=False)

    class Meta:
        model = Cliente
        fields = ('nome', 'cpf','tipo_cnh', 'phone', 'email')