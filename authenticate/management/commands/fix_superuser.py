from django.core.management.base import BaseCommand

from django.contrib.auth import get_user_model



class Command(BaseCommand):
    help = 'Data da Base do SuperUser'

    def handle(self, **options):
        self.stdout.write('Criando dados Gerais de SuperUser')

        User = get_user_model()

        superuser = User.objects.create_superuser(email='admin@email.com.br', password='123123')      


