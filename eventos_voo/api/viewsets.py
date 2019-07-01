from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from eventos_voo.models import EventoVoo
from .serializers import EventoVooSerializer

class EventoVooViewSet(ModelViewSet):

    queryset = EventoVoo.objects.all()
    serializer_class = EventoVooSerializer
    filter_fields = ('nome',)
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication, )