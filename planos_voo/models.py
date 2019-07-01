from django.db import models
from django.core.validators import RegexValidator

class PlanoVoo (models.Model):

    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', "Somente caracterres alfanumericos")
    horaValidador = RegexValidator(r'^[0-9]*$', "Duracao em horas")

    idAeronave = models.CharField(max_length=7, validators=[alphanumeric], null=True)
    numeroDeAeronaves = models.IntegerField(null=True)
    tipoAeronave = models.CharField(max_length=4, validators=[alphanumeric], null=True)
    equipamentoCapacidade = models.CharField(max_length=20, null=True)
    aerodromoPartida = models.CharField(max_length=4, null=True)
    hora = models.TimeField(null=True)
    velocidadeCruzeiro = models.CharField(max_length=5, null=True)
    nivel = models.CharField(max_length=4, null=True)
    rota = models.TextField(null=True)
    aerodromoDestino = models.CharField(max_length=4, null=True)
    duracaoHoras = models.CharField(max_length=2, null=True)
    duracaoMinutos = models.CharField(max_length=2, null=True)
    aerodromoAlternativo = models.CharField(max_length=4, null=True, blank=True)
    outrosDados = models.TextField(null=True, blank=True)
    autonomiaHoras = models.CharField(max_length=2, null=True, validators=[horaValidador])
    pessoasABordo = models.IntegerField(null=True)
    corMarca = models.CharField(max_length=100, null=True)
    piloto = models.CharField(max_length=100, null=True)
    idPlanoVoo = models.CharField(max_length=10, null=True)
    data = models.DateField(null=True)


    def __str__(self):
        return self.idPlanoVoo

