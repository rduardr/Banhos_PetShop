from typing import Any
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class Command(BaseCommand):
    help = "Cria um novo token para ser usado"

    def add_arguments(self, parser):
        parser.add_argument("--username", required=True)
        parser.add_argument("--password", required=True)

    def handle(self, *args: Any, **options):
        username = options["username"]
        password = options["password"]

        self.stdout.write(self.style.WARNING(f"Verificando usuário com o nome {username}"))

        # Verifica se o usuário já existe
        user, created = User.objects.get_or_create(username=username, defaults={'first_name': username})
        if created:
            user.set_password(password)
            user.save()
            self.stdout.write(self.style.SUCCESS(f"Usuário {username} criado com sucesso"))
        else:
            self.stdout.write(self.style.WARNING(f"Usuário {username} já existe"))

        self.stdout.write(self.style.WARNING("Criando token para o usuário"))

        # Cria ou obtém o token
        token, _ = Token.objects.get_or_create(user=user)
        self.stdout.write(self.style.SUCCESS(f"Token criado para o usuário: {token.key}"))
