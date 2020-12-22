from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class downloader(models.Model):
    name = models.TextField(max_length=50, blank=True, null=True, default=None)
    topic = models.TextField(blank=True, null=True, default=None)
    text = models.TextField(blank=True, null=True, default=None)

    def __str__(self):
        # выводим текст поста
        return self.text
