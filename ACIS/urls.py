"""ACIS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from rest_framework.authtoken.views import obtain_auth_token
from informacoes_voo.api.viewsets import InformacoesVooViewSet
from planos_voo.api.viewsets import PlanosVooViewSet

router = routers.DefaultRouter()
router.register(r'informacoesvoo', InformacoesVooViewSet)
router.register(r'planosvoo', PlanosVooViewSet)

schema_view = get_schema_view(title='ACIS API')

urlpatterns = [
    path('esquema/', schema_view),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token)
]
