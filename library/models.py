from django.db import models
from django.contrib.auth.models import User

class MediaItem(models.Model):
    MEDIA_TYPES = [
        ('movie', 'Фильм'),
        ('series', 'Сериал'),
        ('anime', 'Аниме'),
        ('drama', 'Дорама'),
        ('other', 'Другое'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='media_items')
    title = models.CharField(max_length=255)
    media_type = models.CharField(max_length=20, choices=MEDIA_TYPES, default='other')
    seasons = models.PositiveIntegerField(default=1, verbose_name="Сезон")
    total_episodes = models.PositiveIntegerField(default=1, verbose_name="Всего эпизодов")
    watched_episodes = models.PositiveIntegerField(default=0, verbose_name="Просмотрено эпизодов")
    genre = models.CharField(max_length=100, blank=True, null=True, verbose_name="Жанр")
    cover_image = models.ImageField(upload_to='media_items/covers/', blank=True, null=True)
    added_at = models.DateTimeField(auto_now_add=True)

    def progress_percent(self):
        if self.total_episodes == 0:
            return 0
        return round((self.watched_episodes / self.total_episodes) * 100)

    def __str__(self):
        return f"{self.title} ({self.get_media_type_display()})"
