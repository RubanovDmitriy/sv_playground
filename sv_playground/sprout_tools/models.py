from django.db import models
from datetime import timedelta


class Video(models.Model):
    video_id = models.CharField(
        'Video ID',
        max_length=20,
        unique=True,
    )
    title = models.CharField('Название', max_length=100)
    folder_id = models.CharField(
        'Уровень',
        max_length=20,
        default='')
    description = models.CharField(
        'Описание',
        max_length=500,
        null=True,
        blank=True
    )
    duration = models.DurationField('Продолжительность', default=timedelta(seconds=1.0))
    video_link = models.URLField('Ссылка', max_length=300)
    privacy_type = models.IntegerField('Тип доступа')
    tags = models.JSONField('Тэги',)
    created_at = models.DateTimeField(
        'Создано',
        auto_now_add=False,
        auto_now=False,
    )
    updated_at = models.DateTimeField(
        'Обновлено',
        auto_now_add=False,
        auto_now=False,
    )
    plays = models.IntegerField(
        'Количество проигрываний',
        default=0,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'


class Folder(models.Model):
    folder_id = models.CharField(
        'Folder ID',
        max_length=15,
        unique=True,
    )
    name = models.CharField('Название', max_length=100)
    created_at = models.DateTimeField(
        'Создано',
        auto_now_add=False,
        auto_now=False,
    )
    updated_at = models.DateTimeField(
        'Обновлено',
        auto_now_add=False,
        auto_now=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Folder'
        verbose_name_plural = 'Folders'
