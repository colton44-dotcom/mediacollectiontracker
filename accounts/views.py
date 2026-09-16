from django.shortcuts import render, redirect
from django.contrib.auth import login
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