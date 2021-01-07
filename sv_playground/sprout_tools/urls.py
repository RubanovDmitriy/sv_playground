from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('videos', views.videos, name='videos'),
    path('folders', views.folders, name='folders'),
]
