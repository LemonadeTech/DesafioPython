from car_location.location.models.categoriaveiculo import CategoriaVeiculo
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
