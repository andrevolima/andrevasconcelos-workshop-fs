from rest_framework import viewsets
from django.shortcuts import render
from fabrica.models import clientes, colaboradores
from fabrica.serializers import clientesSerializer, colaboradoresSerializer

class clientesViewSet(viewsets.ModelViewSet):
    queryset = clientes.objects.all()
    serializer_class = clientesSerializer

class colaboradoresViewSet(viewsets.ModelViewSet):
    queryset = colaboradores.objects.all()
    serializer_class = colaboradoresSerializer




