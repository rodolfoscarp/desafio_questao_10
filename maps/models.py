from django.db import models


class Locais(models.Model):
    nome = models.CharField('nome', max_length=100, null=False, blank=False)
    latitude = models.FloatField('latitude', null=False, blank=False)
    longitude = models.FloatField('longitude', null=False, blank=False)
    data_expiracao = models.DateField(
        'data_expiracao', null=False, blank=False)

    def __str__(self) -> str:
        return self.nome
