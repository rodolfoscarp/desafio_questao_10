from django.db import models


class Alvo(models.Model):
    identificador = models.AutoField('identificador')
    nome = models.CharField('nome', max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    data_expiracao = models.DateField()
