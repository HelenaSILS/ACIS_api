from rest_framework.viewsets import ModelViewSet
from informacoes_voo.models import InformacoesVoo
from planos_voo.models import PlanoVoo
from .serializers import InformacoesVooSerializer
from .serializers import PlanoVooSerializer

class InformacoesVooViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = InformacoesVoo.objects.all()
    serializer_class = InformacoesVooSerializer


class PlanosVooViewSet(ModelViewSet):
    queryset = PlanoVoo.objects.all()
    serializer_class = PlanoVooSerializer