from rest_framework.serializers import ModelSerializer
from planos_voo.models import PlanoVoo

class PlanoVooSerializer (ModelSerializer):
    class Meta:
        model = PlanoVoo
        fields = ('idPlanoVoo', 'data')