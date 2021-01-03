import requests
import os
from pathlib import Path
from typing import Generator
from urllib.parse import urljoin
from dataclasses import dataclass
from datetime import timedelta
from dotenv import load_dotenv
from sprout_tools.sprout_utills import handle_embedded_code

load_dotenv()


@dataclass
class VideoDataClass:
    video_id: str
    title: str
    folder_id: str
    description: str
    duration: float
    video_link: str
    privacy_type: int
    tags: list
    created_at: str
    updated_at: str
    plays: int


@dataclass
class FolderDataClass:
    folder_id: str
    name: str
    parent_id: str
    created_at: str
    updated_at: str


DOMAIN = 'https://api.sproutvideo.com/'
env_path = Path('/PycharmProjects/sv_playground/sv_playground/') / '.env'
load_dotenv(dotenv_path=env_path)
KEY = os.getenv("SPROUT_API_KEY")


class SproutApiClient:
    def get_videos(self) -> Generator[VideoDataClass, None, None]:
        url = urljoin(DOMAIN, 'v1/videos/')
        while url:
            page = self.get_page(url)

            for raw_video in page.get('videos'):
                yield VideoDataClass(
                    video_id=raw_video['id'],
                    title=raw_video['title'],
                    folder_id=raw_video['folder_id'],
                    description=raw_video['description'],
                    duration=timedelta(raw_video['duration']),
                    video_link=handle_embedded_code(raw_video['embed_code']),
                    privacy_type=raw_video['privacy'],
                    tags=raw_video['tags'],
                    created_at=raw_video['created_at'],
                    updated_at=raw_video['updated_at'],
                    plays=raw_video['plays'],
                )

            url = page.get('next_page')

    def get_folders(self) -> Generator[FolderDataClass, None, None]:
        url = urljoin(DOMAIN, 'v1/folders/')
        page = self.get_page(url)

        for raw_folders in page.get('folders'):
            yield FolderDataClass(
                folder_id=raw_folders['id'],
                name=raw_folders['name'],
                parent_id=raw_folders['parent_id'],
                created_at=raw_folders['created_at'],
                updated_at=raw_folders['updated_at'],
            )

    def get_one_video(self) -> Generator[VideoDataClass, None, None]:
        url = urljoin(DOMAIN, 'v1/videos/4c9ddcb51014e7c4c4')
        while url:
            page = self.get_page(url)

            yield VideoDataClass(
                    video_id=page['id'],
                    title=page['title'],
                    folder_id=page['folder_id'],
                    description=page['description'],
                    duration=timedelta(page['duration']),
                    video_link=handle_embedded_code(page['embed_code']),
                    privacy_type=page['privacy'],
                    tags=page['tags'],
                    created_at=page['created_at'],
                    updated_at=page['updated_at'],
                    plays=page['plays'],
                )

            url = page.get('next_page')

    def get_page(self, url):
        response = requests.get(
            url,
            headers={'SproutVideo-Api-Key': KEY},
            data={'per_page': 100},
        )

        res_json = response.json()

        return res_json

    def set_payload(self):
        # dictx = {'a': 'a',
        #          'b': 'b',
        #          'video_id': None}
        #
        # result = []
        #
        # for video in client.get_videos():
        #     # print(video)
        #
        #     dicty = copy(dictx)
        #     dicty['video_id'] = video.id
        #     result.append(copy(dicty))
        #
        #     print(result)
        pass
