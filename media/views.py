from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import MediaItemForm


def add_media(request):
    if request.method == 'POST':
        form = MediaItemForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Media added successfully!')
            return redirect('add_media')
    else:
        form = MediaItemForm()

    return render(request, 'media/add_media.html', {'form': form})