from django.db import models
from planos_voo.models import PlanoVoo
from eventos_voo.models import EventoVoo
#from registro_comunicacao.models import RegistroComunicacao

class InformacoesVoo (models.Model):
    idInfo = models.TextField(null=True)
    #registroComunicacao = models.ManyToManyField(RegistroComunicacao)
    data = models.DateField()
    planosVoo = models.ManyToManyField(PlanoVoo)
    eventosVoo = models.ManyToManyField(EventoVoo)


    def __str__(self):
        return self.idInfo
