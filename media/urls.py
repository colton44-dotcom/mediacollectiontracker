from django.urls import path
from . import views

urlpatterns = [
    path('add-media/', views.add_media, name='add_media'),
]