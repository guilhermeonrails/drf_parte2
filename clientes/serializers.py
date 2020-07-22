from rest_framework import serializers
from clientes.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    def validate_celular(self, celular):
        if len(celular) != 9:
            raise serializers.ValidationError("O número de celular deve ter 9 dígitos")
        return celular
    def validate_nome(self, nome):
        if nome.replace(" ", "").isalpha():
            raise serializers.ValidationError("Nome inválido")
        return nome