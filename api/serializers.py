from rest_framework.serializers import ModelSerializer
from informacoes_voo.models import InformacoesVoo

class InformacoesVooSerializer (ModelSerializer):
    class Meta:
        model = InformacoesVoo
        fields = ('data', 'registroComunicacao', 'planosVoo')