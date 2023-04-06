from django.db import models

class setores (models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)


    def __str__(self):
        return self.tipo
    
class clientes (models.Model):
    nome = models.CharField(max_length=100)
    idade = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class fornecedores (models.Model):
    nome = models.CharField(max_length=100)
    area = models.ForeignKey("setores", on_delete=models.CASCADE, related_name='fornecedores')
    endereco = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class produtos (models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

