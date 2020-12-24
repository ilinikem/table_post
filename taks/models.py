from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class user(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=50)
    username = models.TextField(blank=True, null=True, default=None)
    email = models.EmailField()
    address = models.JSONField()
    phone = models.TextField()
    website = models.URLField()
    company = models.JSONField()

    def __str__(self):
        # выводим текст поста
        return self.name


class downloader(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.ForeignKey(user, on_delete=models.CASCADE)
    topic = models.TextField(blank=True, null=True, default=None)
    text = models.TextField(blank=True, null=True, default=None)

    def __str__(self):
        # выводим текст поста
        return self.text
