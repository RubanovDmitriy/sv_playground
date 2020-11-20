from django.db import models
from datetime import timedelta


class Video(models.Model):
    video_id = models.CharField('Video ID', max_length=50)
    title = models.CharField('Название', max_length=100)
    description = models.CharField(
        'Описание',
        max_length=500,
        null=True,
        blank=True
    )
    duration = models.DurationField('Продолжительность', default=timedelta(seconds=6300.0))
    video_link = models.URLField('Ссылка', max_length=300)
    privacy_type = models.IntegerField('Тип доступа',)
    tags = models.JSONField('Тэги',)
    created_at = models.DateTimeField(
        'Создано',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Обновлено',
        auto_now=True
    )
    plays = models.IntegerField(
        'Количество проигрываний',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
