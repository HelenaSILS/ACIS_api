from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('PlanosVooViewSet', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })

