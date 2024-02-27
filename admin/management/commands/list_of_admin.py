from typing import Any
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'List all admin user'

    def handle(self, *args: Any, **options: Any):
        admin_user = User.objects.filter(is_superuser=True)
        self.stdout.write('Admin users:')
        for user in admin_user:
            self.stdout.write(f"- {user.username}")