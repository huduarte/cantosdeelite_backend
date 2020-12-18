from rest_framework import viewsets 

from django.conf import settings

from .serializers import PessoaSerializer 
from .models import Pessoa
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework import status, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class PessoaListView(ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    model = Pessoa
    queryset =  Pessoa.objects.all() 
    serializer_class = PessoaSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('uuid', 'email',)

class PessoaUpdateView(RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny,)   
    serializer_class = PessoaSerializer
    lookup_field = 'uuid'

    def get_object(self):
        uuid = self.kwargs["uuid"]
        return get_object_or_404(Pessoa, uuid=uuid)

    def put(self, request, *args, **kwargs):
        answerable = User.objects.filter(email=request.data['answerable']).first()

        if 'email' in request.data and request.data['email']:
            qs = Pessoa.objects.filter(user__email=request.data['email']).first()
            if qs and not qs.has_app:
                self.prepare_email(request.data['email'])
            elif not qs:
                self.prepare_email(request.data['email'])

        return self.update(request, *args, **kwargs)  