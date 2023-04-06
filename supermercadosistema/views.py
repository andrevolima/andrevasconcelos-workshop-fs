from django.shortcuts import render
from rest_framework import viewsets
from supermercadosistema.models import clientes, fornecedores, produtos, setores
from supermercadosistema.serializer import clientesSerializer, fornecedoresSerializer, produtosSerializer, setoresSerializer

class clientesViewSet(viewsets.ModelViewSet):
    queryset = clientes.objects.all()
    serializer_class = clientesSerializer

class fornecedoresViewSet(viewsets.ModelViewSet):
    queryset = fornecedores.objects.all()
    serializer_class = fornecedoresSerializer

class produtosViewSet(viewsets.ModelViewSet):
    queryset = produtos.objects.all()
    serializer_class = produtosSerializer

class setoresViewSet(viewsets.ModelViewSet):
    queryset = setores.objects.all()
    serializer_class = setoresSerializer