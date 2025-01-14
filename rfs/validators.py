from django.core.exceptions import ValidationError
import re


def validar_telefone(valor):
    # Remove qualquer caractere não numérico
    numeros = re.sub(r'\D', '', valor)
    
    # Verifica se o telefone tem 10 ou 11 dígitos
    if len(numeros) not in [10, 11]:
        raise ValidationError("O telefone deve ter 10 ou 11 dígitos.")
    
    # Verifica se contém apenas números
    if not numeros.isdigit():
        raise ValidationError("O telefone deve conter apenas números.")

def validar_cnpj(cnpj):
    # Remove qualquer caractere não numérico
    cnpj = re.sub(r'\D', '', cnpj)
    
    # Verifica se o CNPJ tem 14 dígitos
    if len(cnpj) != 14:
        raise ValidationError("O CNPJ deve ter 14 dígitos.")
    
    # Verifica se contém apenas números
    if not cnpj.isdigit():
        raise ValidationError("O CNPJ deve conter apenas números.")
    
    
