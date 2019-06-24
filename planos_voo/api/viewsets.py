from rest_framework.viewsets import ModelViewSet
from planos_voo.models import PlanoVoo
from .serializers import PlanoVooSerializer

class PlanosVooViewSet(ModelViewSet):
    queryset = PlanoVoo.objects.all()
    serializer_class = PlanoVooSerializer

    def get_queryset(self):
        idPlanoVoo = self.request.query_params.get('idPlanoVoo', None)
        data = self.request.query_params.get('data', None)

        queryset = PlanoVoo.objects.all()

        if idPlanoVoo:
            queryset = PlanoVoo.objects.filter(idPlanoVoo = idPlanoVoo)

        if data:
            queryset = PlanoVoo.object.filter(data = data)

        return queryset