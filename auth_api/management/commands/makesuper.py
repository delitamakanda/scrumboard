from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        user = get_user_model()

        if not user.objects.filter(username="admin").exists():
            user.objects.create_superuser("admin", "makanda.delita@orange.fr", "admin")
