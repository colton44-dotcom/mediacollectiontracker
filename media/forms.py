from django import forms
from .models import MediaItem


class MediaItemForm(forms.ModelForm):
    class Meta:
        model = MediaItem
        fields = [
            'title',
            'media_type',
            'genre',
            'release_year',
            'personal_rating',
            'status',
            'notes',
        ]