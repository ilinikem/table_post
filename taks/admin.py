from django.contrib import admin
from .models import downloader
# Register your models here.


class DownloadAdmin(admin.ModelAdmin):
    # перечисляем поля, которые должны отображаться в админке
    list_display = ("id", "name", "topic", "text")
    # добавляем интерфейс для поиска по тексту постов
    search_fields = ("topic",)
    # добавляем возможность фильтрации по дате
    list_filter = ("id",)
    empty_value_display = "-пусто-"


admin.site.register(downloader, DownloadAdmin)
