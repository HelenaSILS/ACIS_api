from django.db import models
from planos_voo.models import PlanoVoo

class EventoVoo (models.Model):

    nome = models.CharField(max_length=50, null=True)
    descricao = models.TextField(null=True, blank=True)
    data = models.DateField(auto_now_add=True)
    idPlanoVoo = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.nome