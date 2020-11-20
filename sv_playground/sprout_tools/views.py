from django.shortcuts import render
from .models import Video


def index(request):
    return render(request, 'sprout_tools/index.html', {'title': 'Главная страница'})


def videos(request):
    videos = Video.objects.all()
    return render(request, 'sprout_tools/videos.html', {'title': 'Обучающие видео', 'videos': videos})
