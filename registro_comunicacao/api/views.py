from .serializers import RegistroComunicacaoSerializer
from registro_comunicacao.models import RegistroComunicacao
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


@csrf_exempt
def registroComunicacao_list (request):
    if request.method == 'GET':
        registroComunicacao = RegistroComunicacao.objects.all()
        serializer = RegistroComunicacaoSerializer(registroComunicacao, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RegistroComunicacaoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse (serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)