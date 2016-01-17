from car_location.location.models.categoriaveiculo import CategoriaVeiculo
from car_location.location.models.cliente import Cliente
from car_location.location.models.devolucao import Devolucao
from car_location.location.models.locacao import Locacao
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


class LocacaoForm(forms.ModelForm):

    km_inicial = forms.CharField(label="Km Inicial", required=False)
    veiculo = forms.ModelChoiceField(queryset=Veiculo.objects.filter(disponivel=True), widget=forms.Select(), label="Veículo")

    # def clean(self):
    #
    #     if not self.cleaned_data.get('veiculo'):
    #         print("entrou")
    #         self.cleaned_data['veiculo'] = self.instance.veiculo
    #
    #     return self.cleaned_data

    class Meta:
        model = Locacao
        fields = ('cliente', 'veiculo','data_inicial', 'data_final', 'km_inicial', 'valor', 'devolvido')

class DevolucaoForm(forms.ModelForm):

    class Meta:
        model = Devolucao
        fields = ('locacao', 'km_percorrido')
