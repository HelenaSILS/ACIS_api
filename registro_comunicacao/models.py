from django.db import models
from django.contrib.auth.models import User
from informacoes_voo.models import InformacoesVoo


class RegistroComunicacao(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    informacoesVoo = models.ManyToManyField(InformacoesVoo)

    def __str__(self):
        return self.user.username

    #ordering -> ordenar a ordem em que as instancias aparecem
    class Meta: ordering = ('data',)