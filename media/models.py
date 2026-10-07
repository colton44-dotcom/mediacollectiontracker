from django.db import models


class MediaItem(models.Model):
    MEDIA_TYPES = [
        ('Movie', 'Movie'),
        ('TV Show', 'TV Show'),
        ('Book', 'Book'),
        ('Video Game', 'Video Game'),
        ('Music', 'Music'),
    ]

    STATUS_CHOICES = [
        ('Planned', 'Planned'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Owned', 'Owned'),
    ]

    title = models.CharField(max_length=200)
    media_type = models.CharField(max_length=20, choices=MEDIA_TYPES)
    genre = models.CharField(max_length=100)
    release_year = models.IntegerField(blank=True, null=True)
    personal_rating = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.title