from django.core.management.base import BaseCommand, CommandError
from sprout_tools.models import Folder
from sprout_tools.sprout_api_client import SproutApiClient


class Command(BaseCommand):
    help = 'Get all folders from sproutvideo.com'

    def handle(self, *args, **options):
        client = SproutApiClient()
        folder_model = Folder.objects.all()
        for folder in client.get_folders():
            if folder_model.filter(folder_id=folder.folder_id).exists():
                pass
            else:
                item = Folder(
                    folder_id=folder.folder_id,
                    name=folder.name,
                    created_at=folder.created_at,
                    updated_at=folder.updated_at,
                )
                item.save()

            self.stdout.write(self.style.SUCCESS(f'{folder.name} is successfully extracted'))
