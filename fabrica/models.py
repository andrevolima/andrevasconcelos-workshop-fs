from django.db import models

class clientes (models.Model):
    nome = models.CharField(max_length=100)
    area = models.CharField(max_length=100, default='SOME STRING')
    projetos = models.CharField(max_length=100, default='SOME STRING')

    def _str_(self):
        return self.nome
    

class colaboradores (models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=40)
    curso = models.CharField(max_length=40)

    def _str_(self):
        return self.nome

