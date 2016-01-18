from car_location.location.models.categoriaveiculo import CategoriaVeiculo
from car_location.location.models.cliente import Cliente
from car_location.location.models.devolucao import Devolucao
from car_location.location.models.locacao import Locacao
from car_location.location.models.reserva import Reserva
from car_location.location.models.veiculo import Veiculo
from django import forms
from django.core.exceptions import ValidationError

__author__ = 'lucas'


class CategoriaVeiculoForm(forms.ModelForm):

    def clean_nome(self):
        return self.cleaned_data.get('nome').lower()

    def clean_tipo_cnh(self):
        return self.cleaned_data.get('tipo_cnh').upper()

    def clean(self):
        if not self.instance.pk:
            cat_veiculo = CategoriaVeiculo.objects.filter(nome = self.cleaned_data.get('nome').lower())
            if cat_veiculo:
                raise ValidationError('Já existe uma categoria com esse nome')

        return self.cleaned_data

    class Meta:
        model = CategoriaVeiculo
        fields = ('nome', 'tipo_cnh',)
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12 active', 'placeholder': 'ex: carro'}),
            'tipo_cnh':   forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12 active','placeholder': 'ex: B, C separando por "," se for > 1 '}),

        }


class VeiculoForm(forms.ModelForm):

    def clean_modelo(self):
        return self.cleaned_data.get('modelo').lower()

    def clean(self):
        if not self.instance.pk:
            veiculo = Veiculo.objects.filter(modelo=self.cleaned_data.get('modelo').lower(),categoria=self.cleaned_data.get('categoria'))
            if veiculo:
                raise ValidationError('Já existe um veículo com esse nome e categoria')

        return self.cleaned_data


    class Meta:
        model = Veiculo
        fields = ('modelo', 'categoria','quilometragem', 'disponivel')
        widgets = {
            'modelo': forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12 active', 'placeholder': 'ex: Palio'}),
            'categoria':   forms.Select(attrs={'class': 'form-control'}),
            'quilometragem' : forms.NumberInput(attrs={'class': 'form-control col-md-7 col-xs-12'})

        }


class ClienteForm(forms.ModelForm):
    email = forms.EmailField(label="Email", required=False, widget=forms.EmailInput(attrs={'class': 'form-control','placeholder': 'ex: email@gmail.com'}))
    phone = forms.CharField(label="Telefone", required=False, widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'ex: (xx)-999999999'}))

    class Meta:
        model = Cliente
        fields = ('nome', 'cpf','tipo_cnh', 'phone', 'email')
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12 active', 'placeholder': 'ex: Lucas'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12 active', 'placeholder': 'ex: 12345678901'}),
            'tipo_cnh': forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12 active', 'placeholder': 'ex: A,B separando por "," se for > 1'}),

        }

class LocacaoForm(forms.ModelForm):

    km_inicial = forms.CharField(label="Km Inicial", required=False)
    veiculo = forms.ModelChoiceField(queryset=Veiculo.objects.filter(disponivel=True), widget=forms.Select(attrs={'class': 'form-control'}), label="Veículo")

    def set_veiculo(self, queryset, empty_label=None):
        self.fields['veiculo'] = forms.ModelChoiceField(queryset=queryset, widget=forms.Select(attrs={'class':'form-control'}), label="Veículo",  empty_label=empty_label)
        self.base_fields['veiculo'] = forms.ModelChoiceField(queryset=queryset, widget=forms.Select(attrs={'class':'form-control'}), label="Veículo",  empty_label=empty_label)

    def set_cliente(self, queryset, empty_label=None):
        self.fields['cliente'] = forms.ModelChoiceField(queryset=queryset, widget=forms.Select(attrs={'class':'form-control'}), label="Cliente",  empty_label=empty_label)
        self.base_fields['cliente'] = forms.ModelChoiceField(queryset=queryset, widget=forms.Select(attrs={'class':'form-control'}), label="Cliente",  empty_label=empty_label)

    def clean(self):
        cliente, veiculo = self.cleaned_data.get('cliente'), self.cleaned_data.get('veiculo')
        if cliente and veiculo:
            tipo_cnh_cliente, permissao_veiculo_cnh = cliente.tipo_cnh, veiculo.categoria.tipo_cnh
            permission = False
            for p in permissao_veiculo_cnh.split(","):
                if p.strip() in [ t.strip() for t in tipo_cnh_cliente.split(",")]:
                    permission = True
                    break
            if not permission:
                raise ValidationError('O cliente não Possui habilitação para conduzir esse veículo')

        return self.cleaned_data


    class Meta:
        model = Locacao
        fields = ('cliente', 'veiculo','data_inicial', 'data_final', 'km_inicial', 'valor', 'devolvido')
        widgets = {
            'data_inicial': forms.DateInput(attrs={'class': 'date-picker form-control col-md-7 col-xs-12 active', 'placeholder': 'ex: DD/MM/YYY'}),
            'data_final':   forms.DateInput(attrs={'class': 'date-picker form-control col-md-7 col-xs-12 active', 'placeholder': 'ex: DD/MM/YYY'}),
            'cliente':   forms.Select(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control col-md-7 col-xs-12'})
        }


class DevolucaoForm(forms.ModelForm):

    locacao = forms.ModelChoiceField(queryset=Locacao.objects.filter(devolvido=False), widget=forms.Select(attrs={'class':'form-control'}), label="Locação",  empty_label=None)

    def set_locacao(self, queryset):
        self.fields['locacao'] = forms.ModelChoiceField(queryset=queryset, widget=forms.Select(attrs={'class':'form-control'}), label="Locação",  empty_label=None)
        self.base_fields['locacao'] = forms.ModelChoiceField(queryset=queryset, widget=forms.Select(attrs={'class':'form-control'}), label="Locação")


    class Meta:
        model = Devolucao
        fields = ('locacao', 'km_percorrido')
        widgets = {
            'km_percorrido': forms.NumberInput(attrs={'class': 'form-control col-md-7 col-xs-12'})
        }


class ReservaForm(forms.ModelForm):

    veiculo = forms.ModelChoiceField(queryset=Veiculo.objects.filter(disponivel=False), widget=forms.Select(attrs={'class':'form-control'}), label="Veículo")

    def set_veiculo(self, queryset, empty_label=None):
        self.fields['veiculo'] = forms.ModelChoiceField(queryset=queryset,
                                                        widget=forms.Select(attrs={'class':'form-control'}), label="Veículo",  empty_label=empty_label)
        self.base_fields['veiculo'] = forms.ModelChoiceField(queryset=queryset,
                                                             widget=forms.Select(attrs={'class':'form-control'}), label="Veículo",  empty_label=empty_label)

    def set_cliente(self, queryset, empty_label=None):
        self.fields['cliente'] = forms.ModelChoiceField(queryset=queryset,
                                                        widget=forms.Select(attrs={'class':'form-control'}), label="Cliente",  empty_label=empty_label)
        self.base_fields['cliente'] = forms.ModelChoiceField(queryset=queryset,
                                                             widget=forms.Select(attrs={'class':'form-control'}), label="Cliente",  empty_label=empty_label)

    def clean(self):
        cliente, veiculo = self.cleaned_data.get('cliente'), self.cleaned_data.get('veiculo')
        if cliente and veiculo:
            reserva = Reserva.objects.filter(cliente=self.cleaned_data.get('cliente'),
                                         veiculo=self.cleaned_data.get('veiculo'),finalizada=False)
            if reserva:
                if reserva[0] != self.instance:
                    raise ValidationError('O cliente Já tem uma reserva aberta para esse veículo.')

            tipo_cnh_cliente, permissao_veiculo_cnh = cliente.tipo_cnh, veiculo.categoria.tipo_cnh
            permission = False
            for p in permissao_veiculo_cnh.split(","):
                if p.strip() in [ t.strip() for t in tipo_cnh_cliente.split(",")]:
                    permission = True
                    break
            if not permission:
                raise ValidationError('O cliente não Possui habilitação para conduzir esse veículo')
            if cliente.email == "":
                raise ValidationError('Adicone um endereço de email ao cliente para efetuar a reserva')

        return self.cleaned_data


    class Meta:
        model = Reserva
        fields = ('nome', 'veiculo', 'cliente', 'finalizada')
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12 active', 'placeholder': 'ex: Nome da Reserva'}),
            'veiculo':   forms.Select(attrs={'class': 'form-control'}),
            'cliente':   forms.Select(attrs={'class': 'form-control'}),
        }