import pytz
import uuid
import random
import datetime
import datetime as date

from django.core.management.base import BaseCommand
from django.contrib.auth.models import  Permission
from django.contrib.auth import authenticate, get_user_model

from unittest import mock

from pessoa.models import Pessoa

User = get_user_model()

MAX_RANGE = 30


class Command(BaseCommand):
    help = 'Data da Base do Pessoa'

    def handle(self, **options):
        self.stdout.write('Criando dados Gerais de Pessoa')

        user_a = User.objects.get(email='hudsoneeto@outlook.com')

        for x in range(1,MAX_RANGE):
            mocked = datetime.datetime(2018, 4, 4, 0, 0, 0, tzinfo=pytz.utc)
            with mock.patch('django.utils.timezone.now', mock.Mock(return_value=mocked)):
                Pessoa.objects.create(
                    uuid = uuid.uuid4(), 
                    email = 'hudsoneeto@outlook.com',
                    name = 'Hudson'
                )

        for x in range(1,MAX_RANGE):
            mocked = datetime.datetime(2020, 9, random.randint(1,12), 0, 0, 0, tzinfo=pytz.utc)
            with mock.patch('django.utils.timezone.now', mock.Mock(return_value=mocked)):            
                Pessoa.objects.create(
                    uuid = uuid.uuid4(), 
                    email = 'hudsoneeto@outlook.com',
                    name = 'Hudson'
                ) 
                Pessoa.objects.create(
                    uuid = uuid.uuid4(), 
                    email = 'hudsoneeto@outlook.com',
                    name = 'Hudson'
                )                 

            mocked = datetime.datetime(2020, random.randint(1,12), random.randint(1,29), 0, 0, 0, tzinfo=pytz.utc)
            with mock.patch('django.utils.timezone.now', mock.Mock(return_value=mocked)):            
                Pessoa.objects.create(
                    uuid = uuid.uuid4(), 
                    email = 'hudsoneeto@outlook.com',
                    name = 'Hudson'
                )                 