from django import forms
from .models import Media


class MediaItemForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = [
            'title',
            'media_type',
            'genre',
            'release_year',
            'status',
            'rating',        
            'notes',
        ]
        