from rest_framework import serializers
from clientes.models import Cliente
from .validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    #Validação no serializers
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"Número de CPF inválido."})

        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':"O nome deve conter apenas letras."})
        
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':"O RG deve conter nove digitos."})
        
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':"exemplo válido xx xxxxx-xxxx"})
        
        return data
