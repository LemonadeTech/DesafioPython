from django import forms
__author__ = 'lucas'


class LoginForm(forms.Form):
    username = forms.CharField(label="Usuário")
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(render_value=False))
