from django.core.management.base import BaseCommand, CommandError
# from sv_playground.sprout_tools.models import Video
from sprout_tools.sprout_api_client import SproutApiClient


class Command(BaseCommand):
    help = 'Get all videos from sproutvideo.com'

    def handle(self, *args, **options):
        client = SproutApiClient()
        for video in client.get_one_video():
            print(video)

            self.stdout.write(self.style.SUCCESS(f'{video} is successfully printed'))
