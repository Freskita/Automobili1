from rest_framework import serializers 
from .models import Marca, Cliente, Auto, Concessionario, Acquisto



class MarcaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Marca 
        fields = '__all__'


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class AutoSerializer(serializers.ModelSerializer):
    marca = MarcaSerializer()

    class Meta:
        model = Auto
        fields = '__all__'

class ConcessionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concessionario
        fields = '__all__'

class AcquistoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acquisto
        fields = '__all__'
