from rest_framework.serializers import HyperlinkedModelSerializer
from informacoes_voo.models import InformacoesVoo

class InformacoesVooSerializer (HyperlinkedModelSerializer):
    class Meta:
        model = InformacoesVoo
        fields = ('data', 'Info', 'planosVoo', 'eventosVoo')


