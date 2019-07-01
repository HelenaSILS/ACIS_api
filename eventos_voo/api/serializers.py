from rest_framework.serializers import HyperlinkedModelSerializer
from eventos_voo.models import EventoVoo

class EventoVooSerializer (HyperlinkedModelSerializer):
    class Meta:
        model = EventoVoo
        fields = ('nome', 'descricao', 'data')