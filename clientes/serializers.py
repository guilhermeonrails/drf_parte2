from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate(self, data):
        if not caracteres_alfabeticos(data['nome']):
            raise serializers.ValidationError({"nome": "Nome inválido: não inclua números"})
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({"cpf": "CPF inválido"})
        if not quantidade_de_digitos(data['rg'], 9):
            raise serializers.ValidationError({"rg": "RG inválido. O RG deve conter 9 dígitos"})
        if not numero_celular_valido(data['celular']):
            raise serializers.ValidationError({"celular": "O celular deve conter 11 dígitos, sendo 2, um espaço, 5 dígitos, uma seta e os 4 ultimos, como ilustra o exemplo: 11 99999-9999"})
        return data

    # def validate_cpf(self, cpf):
    #     if len(cpf) != 11:
    #         raise serializers.ValidationError("O CPF deve conter 11 dígitos")
    #     return celular
    # def validate_nome(self, nome):
    #     if nome.replace(" ", "").isalpha():
    #         raise serializers.ValidationError("Nome inválido")
    #     return nome