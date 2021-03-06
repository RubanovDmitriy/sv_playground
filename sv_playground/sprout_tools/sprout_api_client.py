import requests
import os
from pathlib import Path
from typing import Generator
from urllib.parse import urljoin
from dataclasses import dataclass
from datetime import timedelta
from dotenv import load_dotenv
from sprout_tools.sprout_utills import handle_embedded_code, create_video_payload
import json

load_dotenv()


@dataclass
class VideoDataClass:
    video_id: str
    title: str
    folder_id: str
    description: str
    duration: timedelta
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
    created_at: str
    updated_at: str


@dataclass
class LoginDataClass:
    login_id: str
    email: str
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
                created_at=raw_folders['created_at'],
                updated_at=raw_folders['updated_at'],
            )

    def get_logins(self) -> Generator[LoginDataClass, None, None]:
        url = urljoin(DOMAIN, 'v1/logins/')
        while url:
            page = self.get_page(url)

            for raw_login in page.get('logins'):
                yield LoginDataClass(
                    login_id=raw_login['id'],
                    email=raw_login['email'],
                    created_at=raw_login['created_at'],
                    updated_at=raw_login['updated_at'],
                )

            url = page.get('next_page')

    @staticmethod
    def post_login(email, password):
        url = urljoin(DOMAIN, 'v1/logins')
        payload = {
            "email": email,
            "password": password
        }
        json_payload = json.dumps(payload)
        r = requests.post(
            url,
            headers={'SproutVideo-Api-Key': KEY},
            data=json_payload
        )
        if r.status_code == 201:
            return True
        return False

    @staticmethod
    def delete_login(login_id):
        url = urljoin(DOMAIN, f'v1/logins/{login_id}')
        r = requests.delete(
            url,
            headers={'SproutVideo-Api-Key': KEY},
        )
        print(r.status_code)
        if r.status_code == 200:
            return True
        return False

    def get_page(self, url):
        response = requests.get(
            url,
            headers={'SproutVideo-Api-Key': KEY},
            data={'per_page': 100},
        )

        res_json = response.json()

        return res_json

    def post_access_grants(self, login_id, access='all'):
        url = urljoin(DOMAIN, 'v1/access_grants/bulk')
        body = create_video_payload(login_id, access)
        for payload in body:
            json_payload = json.dumps(payload)
            r = requests.post(
                url,
                headers={'SproutVideo-Api-Key': KEY},
                data=json_payload
            )
