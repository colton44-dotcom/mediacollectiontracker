from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import MediaItemForm
from django.db.models import Count, Q
from django.shortcuts import render
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


@login_required
def media_status_report(request):
    media_items = Media.objects.filter(user=request.user)

    status_counts = [
        {
            'name': label,
            'count': media_items.filter(status=value).count()
        }
        for value, label in Media.STATUS_CHOICES
    ]

    context = {
        'status_counts': status_counts,
        'total_media': media_items.count(),
    }

    return render(request, 'media/status_report.html', context)

@login_required
def media_collection_summary(request):
    user_items = Media.objects.filter(user=request.user)

    # One group-by query: counts per media_type
    raw = (
        user_items
        .values('media_type')
        .annotate(
            total=Count('id'),
            completed=Count('id', filter=Q(status='Completed')),
            in_progress=Count('id', filter=Q(status='In Progress')),
        )
    )
    by_type = {row['media_type']: row for row in raw}

    # Iterate the model's choices so zero-count categories still appear
    choices = list(Media._meta.get_field('media_type').choices or [])
    if not choices:
        choices = [(v, v) for v in user_items.values_list('media_type', flat=True).distinct()]

    report = []
    totals = {'total': 0, 'completed': 0, 'in_progress': 0}

    for value, label in choices:
        row = by_type.get(value, {})
        entry = {
            'media_type': value,
            'label': label,
            'total': row.get('total', 0),
            'completed': row.get('completed', 0),
            'in_progress': row.get('in_progress', 0),
        }
        report.append(entry)
        totals['total'] += entry['total']
        totals['completed'] += entry['completed']
        totals['in_progress'] += entry['in_progress']

    return render(request, 'media/collection_summary.html', {
        'report': report,
        'totals': totals,
    })