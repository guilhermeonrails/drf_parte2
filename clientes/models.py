from django.db import models
from datetime import datetime

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=9)
    rg = models.CharField(max_length=11)
    celular = models.CharField(max_length=11)
    ativo = models.BooleanField(default=False)
    data_cadastro = models.DateTimeField(default=datetime.now, editable=False)

    def __str__(self):
        return self.nome
