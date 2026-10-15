
from django.urls import path
from . import views

urlpatterns = [
    path('add-media/', views.add_media, name='add_media'),
    path('edit-media/<int:media_id>/', views.edit_media, name='edit_media'),
    path('delete-media/<int:media_id>/', views.delete_media, name='delete_media'),
]
