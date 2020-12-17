from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets 
from rest_framework.generics import ListCreateAPIView
from rest_framework import permissions

from .serializers import ConfigSerializer
from core.config.models import Config

class ConfigListView(ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    model = Config
    queryset =  Config.objects.filter(is_active=True)
    serializer_class = ConfigSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'name', 'endpoint','token')