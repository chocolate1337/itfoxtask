from django.contrib import admin
from .models import News

class AdminNews(admin.ModelAdmin):
    list_display = ['title', 'created_at','text_news']


admin.site.register(News,AdminNews)