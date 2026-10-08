from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from media.models import Media
from .forms import CustomUserCreationForm

# Create your views here.
def home(request):
    return render(request, 'accounts/home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Auto login the user after registration
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def dashboard(request):
    user_items = Media.objects.filter(user=request.user)

    context = {
        'total_count': user_items.count(),
        'in_progress': user_items.filter(status='In Progress')[:5],
        'recently_added': user_items[:5],  # model Meta already orders by -date_added
        'planned_count': user_items.filter(status='Planned').count(),
        'completed_count': user_items.filter(status='Completed').count(),
    }
    return render(request, 'accounts/dashboard.html', context)
