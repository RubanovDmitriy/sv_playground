from django.core.management.base import BaseCommand
from sprout_tools.sprout_api_client import SproutApiClient


class Command(BaseCommand):
    help = 'Give access to all videos from sproutvideo.com'

    def add_arguments(self, parser):
        parser.add_argument('login_id', type=str)

    def handle(self, *args, **options):
        client = SproutApiClient()
        client.post_access_grants(options['login_id'])

        self.stdout.write(self.style.SUCCESS(f'Accesses successfully granted for login_id {options["login_id"]}'))
