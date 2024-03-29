from rest_framework.serializers import HyperlinkedModelSerializer
from registro_comunicacao.models import RegistroComunicacao
from django.contrib.auth.models import User


class RegistroComunicacaoSerializer (HyperlinkedModelSerializer):

    class Meta:
        model = RegistroComunicacao
        fields = ('id', 'mensagem', 'data')


#class RegistroComunicacaoSerializer (serializers.Serializer):
#    id = serializers.ImageField(read_only=True)
#    user = serializers.HyperlinkedModelSerializer.fields
#    mensagem = serializers.CharField(required=False)
#    data = serializers.DateField()

#    def create(self, validated_data):
#        return RegistroComunicacao.objects.create(**validated_data)

#   def update(self, instance, validated_data):
#        instance.user = validated_data.get('user',instance.user)
#        instance.mensansagem = validated_data.get('mensagem', instance.user)
#        instance.mensansagem = validated_data.get('data', instance.data)
#        instance.save()
#        return instance