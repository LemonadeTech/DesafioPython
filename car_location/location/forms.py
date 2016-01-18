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

    def clean(self):
        cat_veiculo = CategoriaVeiculo.objects.filter(nome = self.cleaned_data.get('nome').lower())
        if cat_veiculo:
            raise ValidationError('Já existe uma categoria com esse nome')

        return self.cleaned_data

    class Meta:
        model = CategoriaVeiculo
        fields = ('nome', 'tipo_cnh',)
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12 active'}),
            'tipo_cnh':   forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12 active'}),

        }


class VeiculoForm(forms.ModelForm):

    def clean_modelo(self):
        return self.cleaned_data.get('modelo').lower()

    def clean(self):
        veiculo = Veiculo.objects.filter(modelo=self.cleaned_data.get('modelo').lower(),categoria=self.cleaned_data.get('categoria'))
        if veiculo:
            raise ValidationError('Já existe um veículo com esse nome e categoria')

        return self.cleaned_data

    class Meta:
        model = Veiculo
        fields = ('modelo', 'categoria','quilometragem', 'disponivel')
        widgets = {
            'modelo': forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12 active'}),
            'categoria':   forms.Select(attrs={'class': 'form-control'}),
            'quilometragem' : forms.NumberInput(attrs={'class': 'form-control col-md-7 col-xs-12'})

        }


class ClienteForm(forms.ModelForm):
    email = forms.EmailField(label="Email", required=False, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label="Telefone", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Cliente
        fields = ('nome', 'cpf','tipo_cnh', 'phone', 'email')
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12 active'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12 active'}),
            'tipo_cnh': forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12 active'}),

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

        tipo_cnh_cliente, permissao_veiculo_cnh = self.cleaned_data.get('cliente').tipo_cnh, self.cleaned_data.get('veiculo').categoria.tipo_cnh
        permission = False
        for p in permissao_veiculo_cnh.split(","):
            if p.strip() in [ t.strip() for t in tipo_cnh_cliente.split(",")]:
                permission = True
                break
        if not permission:
            raise ValidationError('O cliente não Possui habilitação para conduzir esse veículo')


    class Meta:
        model = Locacao
        fields = ('cliente', 'veiculo','data_inicial', 'data_final', 'km_inicial', 'valor', 'devolvido')
        widgets = {
            'data_inicial': forms.DateInput(attrs={'class': 'date-picker form-control col-md-7 col-xs-12 active'}),
            'data_final':   forms.DateInput(attrs={'class': 'date-picker form-control col-md-7 col-xs-12 active'}),
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
        reserva = Reserva.objects.filter(cliente=self.cleaned_data.get('cliente'),
                                         veiculo=self.cleaned_data.get('veiculo'),finalizada=True)
        if reserva:
            raise ValidationError('O cliente Já tem uma reserva aberta para esse veículo.')
        tipo_cnh, permissao_cnh = self.cleaned_data.get('cliente').tipo_cnh, self.cleaned_data.get('veiculo').categoria.tipo_cnh
        if not permissao_cnh in [ tipo for tipo in tipo_cnh]:
            raise ValidationError('O cliente não Possui habilitação para conduzir esse veículo')
        if self.cleaned_data.get('cliente').email == "":
            raise ValidationError('Adicone um endereço de email ao cliente para efetuar a reserva')

    class Meta:
        model = Reserva
        fields = ('nome', 'veiculo', 'cliente', 'finalizada')
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12 active'}),
            'veiculo':   forms.Select(attrs={'class': 'form-control'}),
            'cliente':   forms.Select(attrs={'class': 'form-control'}),
        }