from copy import copy
from bs4 import BeautifulSoup
from sprout_tools.models import Video

MAKE_FOLDER_ID = '3598d8bc131ebe'


def handle_embedded_code(iframe):
    soup = BeautifulSoup(iframe, "html.parser")
    return soup.iframe['src']


def create_payload(login_id):
    video_model = Video.objects.all().order_by('id')

    access_grant_template = {
        "login_id": login_id,
        "video_id": None,
        "allowed_plays": None,
        "access_starts_at": None,
        "access_ends_at": None,
        "download_permissions": [],
    }

    result = []

    for video in video_model:
        if video.folder_id == '3598d8bc131ebe':
            continue
        access_grant = copy(access_grant_template)
        access_grant['video_id'] = video.video_id
        result.append(copy(access_grant))

    paginated_result = chunker(result, 99)

    return paginated_result


def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))
