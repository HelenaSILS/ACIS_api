from rest_framework.viewsets import ModelViewSet
from registro_comunicacao.models import RegistroComunicacao
from .serializers import RegistroComunicacaoSerializer

class RegistroComunicacaoViewSet (ModelViewSet):

    queryset = RegistroComunicacao.objects.all()
    serializer_class = RegistroComunicacaoSerializer
    filter_fields = ('mensagem', 'data')
