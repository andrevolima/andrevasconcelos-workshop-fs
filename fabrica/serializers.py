from rest_framework import serializers
from fabrica.models import clientes, colaboradores

class clientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = clientes
        fields = ['nome', 'area', 'projetos']

class colaboradoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = colaboradores 
        fields = ['nome', 'especialidade', 'curso']




