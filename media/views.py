from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import MediaItemForm
from .models import Media


@login_required
def add_media(request):
    if request.method == 'POST':
        form = MediaItemForm(request.POST)

        if form.is_valid():
            media = form.save(commit=False)
            media.user = request.user
            media.save()

            messages.success(request, 'Media added successfully!')
            return redirect('add_media')
    else:
        form = MediaItemForm()

    return render(request, 'media/add_media.html', {'form': form})


@login_required
def edit_media(request, media_id):
    media = get_object_or_404(Media, id=media_id, user=request.user)

    if request.method == 'POST':
        form = MediaItemForm(request.POST, instance=media)

        if form.is_valid():
            form.save()
            messages.success(request, 'Media updated successfully!')
            return redirect('dashboard')
    else:
        form = MediaItemForm(instance=media)

    return render(request, 'media/edit_media.html', {
        'form': form,
        'media': media
    })


@login_required
def delete_media(request, media_id):
    media = get_object_or_404(Media, id=media_id, user=request.user)

    if request.method == 'POST':
        media.delete()
        messages.success(request, 'Media deleted successfully!')
        return redirect('dashboard')

    return render(request, 'media/delete_media.html', {
        'media': media
    })
