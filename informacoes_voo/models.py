from django.db import models
from planos_voo.models import PlanoVoo
from registro_comunicacao.models import registroComunicacao

class InformacoesVoo (models.Model):
    registroComunicacao = models.ManyToManyField(registroComunicacao)
    data = models.DateField()
    planosVoo = models.ManyToManyField(PlanoVoo)

    def __str__(self):
        return self.data
