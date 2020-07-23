from validate_docbr import CPF
import re

def quantidade_de_digitos(campo, numero_digitos):
    """Valida quantidades de dígitos de um campo"""
    if len(campo) == numero_digitos:
        return True

# Retorne true se todos os caracteres da string forem alfabéticos e 
# houver pelo menos um caractere, caso contrário, false
def caracteres_alfabeticos(campo):
    """Verifica se o campo possui caracteres alfabéticos"""
    if campo.replace(" ", "").isalpha():
        return True

def cpf_valido(numero_cpf):
    """Verifica se o CPF é válido, com base nas regras nacionais"""
    cpf = CPF()
    return cpf.validate(numero_cpf)

def numero_celular_valido(numero_celular):
    """Verifica se o celular é válido (11123451234)"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, numero_celular)
    return resposta