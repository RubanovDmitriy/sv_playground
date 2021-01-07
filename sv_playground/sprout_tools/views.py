from django.shortcuts import render
from .models import Video, Folder


def index(request):
    return render(request, 'sprout_tools/index.html', {'title': 'Главная страница'})


def videos(request):
    videos = Video.objects.all()
    return render(request, 'sprout_tools/videos.html', {'title': 'Обучающие видео', 'videos': videos})


def folders(request):
    folders = Folder.objects.all()
    return render(request, 'sprout_tools/folder.html', {'title': 'Уровни', 'folders': folders})
