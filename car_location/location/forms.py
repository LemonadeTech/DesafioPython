from car_location.location.models.categoriaveiculo import CategoriaVeiculo
from django import forms

__author__ = 'lucas'

# class CategoriaVeiculoForm(forms.Form):
#
#     nome = forms.CharField(label="Nome")
#     tipo_cnh = forms.CharField(label="Cnh Permitida")

class CategoriaVeiculoForm(forms.ModelForm):

    class Meta:
        model = CategoriaVeiculo
        fields = ('nome', 'tipo_cnh',)