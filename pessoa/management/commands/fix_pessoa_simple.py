from django.core.management.base import BaseCommand
from django.contrib.auth.models import  Permission

from django.contrib.auth import authenticate, get_user_model
User = get_user_model()

from pessoa.models import Pessoa
import datetime as date
import uuid

class Command(BaseCommand):
    help = 'Data da Base do Pessoa'

    def handle(self, **options):
        self.stdout.write('Criando dados Gerais de Pessoa')

        for x in range(1,10):
            Pessoa.objects.create(
                uuid = uuid.uuid4(), 
                email = 'hudsoneeto@outlook.com',
                name = 'Hudson',
            )

        for x in range(1,10):
            Pessoa.objects.create(
                uuid = uuid.uuid4(), 
                email = 'hudsoneeto@outlook.com',
                name = 'Hudson',
            )            