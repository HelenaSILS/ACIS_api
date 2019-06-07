from django.db import models

class PlanoVoo (models.Model):
    idPlanoVoo = models.CharField(max_length=10)
    idAeronave = models.CharField(max_length=10)
    tipoAeronave = models.CharField(max_length=50)
    velocidadeCruzeiro = models.DecimalField(decimal_places=1, max_digits=5)
    data = models.DateField()

    def __str__(self):
        return self.idPlanoVoo
