from django.db import models
from django.conf import settings


class Media(models.Model):
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

    RATING_CHOICES = [(i, str(i)) for i in range(1, 11)]  # 1 to 10
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='media_items',
    )
    title = models.CharField(max_length=200)
    media_type = models.CharField(max_length=20, choices=MEDIA_TYPES)
    genre = models.CharField(max_length=100, blank=True)
    release_year = models.IntegerField(blank=True, null=True)
    rating = models.PositiveSmallIntegerField(
        choices=RATING_CHOICES,
        null=True,
        blank=True,
        help_text="Optional: 1–10, or leave blank if unrated.",
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Planned')
    notes = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title
