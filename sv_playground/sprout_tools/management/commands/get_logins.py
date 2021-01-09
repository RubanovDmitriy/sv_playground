from django.core.management.base import BaseCommand, CommandError
from sprout_tools.models import Login
from sprout_tools.sprout_api_client import SproutApiClient


class Command(BaseCommand):
    help = 'Get all logins from sproutvideo.com'

    def handle(self, *args, **options):
        client = SproutApiClient()
        login_model = Login.objects.all()
        login_model.delete()
        for login in client.get_logins():
            if login_model.filter(login_id=login.login_id).exists():
                pass
            else:
                item = Login(
                    login_id=login.login_id,
                    email=login.email,
                    created_at=login.created_at,
                    updated_at=login.updated_at,
                )
                item.save()

            self.stdout.write(self.style.SUCCESS(f'{login.email} is successfully extracted'))
