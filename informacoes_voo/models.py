from django.db import models
from planos_voo.models import PlanoVoo
from eventos_voo.models import EventoVoo
#from registro_comunicacao.models import RegistroComunicacao

class InformacoesVoo (models.Model):
    Info = models.TextField(null=True)
    #registroComunicacao = models.ManyToManyField(RegistroComunicacao)
    data = models.DateField()
    planosVoo = models.ManyToManyField(PlanoVoo, blank=True)
    eventosVoo = models.ManyToManyField(EventoVoo, blank=True)


    def __str__(self):
        return self.idInfo
