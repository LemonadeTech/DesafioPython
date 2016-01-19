from django.core.exceptions import ValidationError

__author__ = 'lucas'


def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('CPF deve conter apenas números','digits')
    if len(value) != 11:
        raise ValidationError('CPF deve conter 11 números', 'length')
