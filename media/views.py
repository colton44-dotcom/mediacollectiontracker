from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import MediaItemForm


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