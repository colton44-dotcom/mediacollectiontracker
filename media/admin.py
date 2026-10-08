from django.contrib import admin
from .models import Media


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'media_type', 'status', 'date_added')
    list_filter = ('media_type', 'status')
    search_fields = ('title', 'genre')
