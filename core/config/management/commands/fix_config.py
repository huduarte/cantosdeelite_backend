from django.core.management.base import BaseCommand
from django.contrib.auth.models import  Permission
from django.contrib.auth import authenticate, get_user_model

from core.config.models import Config


class Command(BaseCommand):
    help = 'Iniciando Configuracao INicial'

    def handle(self, **options):
        self.stdout.write('Criando dados Gerais de Configuracao')

        Config.objects.create(
            name="Inicial",
            endpoint="inicial",
            token="inicial",
            logo_url="inicial",
            about_us="inicial",
            terms="inicial",
            lgpd_terms="inicial",
            febre_number=38
        )
