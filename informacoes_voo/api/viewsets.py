from rest_framework.viewsets import ModelViewSet
from informacoes_voo.models import InformacoesVoo
from .serializers import InformacoesVooSerializer

class InformacoesVooViewSet(ModelViewSet):

    queryset = InformacoesVoo.objects.all()
    serializer_class = InformacoesVooSerializer
    filter_fields = ('Info', 'data')


