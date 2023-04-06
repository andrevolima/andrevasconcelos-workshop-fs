from rest_framework import serializers
from supermercadosistema.models  import clientes, fornecedores, produtos, setores

class clientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = clientes
        fields = ['nome', 'idade', 'email', 'endereco']

class fornecedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = fornecedores
        fields = ['nome', 'area', 'endereco']

class produtosSerializer(serializers.ModelSerializer):
    class Meta:
        model = produtos
        fields = ['nome', 'quantidade']

class setoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = setores
        fields = ['nome','tipo']