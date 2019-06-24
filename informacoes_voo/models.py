from django.db import models
from planos_voo.models import PlanoVoo
from registro_comunicacao.models import RegistroComunicacao

class InformacoesVoo (models.Model):
    idInfo = models.TextField(null=True)
    #registroComunicacao = models.ManyToManyField(registroComunicacao)
    data = models.DateField()
    planosVoo = models.ManyToManyField(PlanoVoo)

    def __str__(self):
        return self.idInfo
