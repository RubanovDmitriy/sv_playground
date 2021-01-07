from django.core.management.base import BaseCommand, CommandError
from sprout_tools.models import Video
from sprout_tools.sprout_api_client import SproutApiClient


class Command(BaseCommand):
    help = 'Get all videos from sproutvideo.com'

    def handle(self, *args, **options):
        client = SproutApiClient()
        video_model = Video.objects.all()
        for video in client.get_videos():
            if video_model.filter(video_id=video.video_id).exists():
                pass
            else:
                item = Video(
                    video_id=video.video_id,
                    title=video.title,
                    folder_id=video.folder_id,
                    description=video.description,
                    duration=video.duration,
                    video_link=video.video_link,
                    privacy_type=video.privacy_type,
                    tags=video.tags,
                    created_at=video.created_at,
                    updated_at=video.updated_at,
                    plays=video.plays,
                )
                item.save()

            self.stdout.write(self.style.SUCCESS(f'{video.title} is successfully extracted'))





