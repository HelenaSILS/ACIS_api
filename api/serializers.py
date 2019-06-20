from rest_framework.serializers import ModelSerializer
from informacoes_voo.models import InformacoesVoo
from planos_voo.models import PlanoVoo

class InformacoesVooSerializer (ModelSerializer):
    class Meta:
        model = InformacoesVoo
        fields = ('data', 'registroComunicacao', 'planosVoo')


class PlanoVooSerializer (ModelSerializer):
    class Meta:
        model = PlanoVoo
        fields = ('idPlanoVoo', 'data')