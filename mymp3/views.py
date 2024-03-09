# yourappname/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import SongForm
from django.http import HttpResponse
from .models import Song
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')  


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()

    return render(request, '/home/sriharsha/django_frac_project/my_music/mymp3/templates/register.html', {'form': form, 'action': 'Register'})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()

    return render(request, '/home/sriharsha/django_frac_project/my_music/mymp3/templates/login.html', {'form': form, 'action': 'Login'})

# def dashboard_view(request):
#     songs = Song.objects.filter(user=request.user)
#     return render(request, '/home/sriharsha/django_frac_project/my_music/mymp3/templates/dashboard.html', {'songs': songs})

def dashboard_view(request):
    # Check if the user is authenticated before filtering songs
    if request.user.is_authenticated:
        user_id = request.user.id
        songs = Song.objects.filter(user_id=user_id)
        return render(request, '/home/sriharsha/django_frac_project/my_music/mymp3/templates/dashboard.html', {'songs': songs})
    else:
        # Handle the case where the user is not authenticated (optional)
        # return render(request, '/home/sriharsha/django_frac_project/my_music/mymp3/templates/dashboard.html', {'songs': []})
        return redirect('login')

def upload_song_view(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            song = form.save(commit=False)
            song.user = request.user
            song.save()
            return redirect('dashboard')
    else:
        form = SongForm()
    return render(request, '/home/sriharsha/django_frac_project/my_music/mymp3/templates/upload_song.html', {'form': form})

def your_audio_view(request, song_id):
    song = Song.objects.get(id=song_id)

    # Make sure the song has audio content
    if song.audio_file_content:
        response = HttpResponse(song.audio_file_content, content_type='audio/mp3')
        response['Content-Disposition'] = f'inline; filename="{song.title}.mp3"'
        return response
    else:
        return HttpResponse("Song not found or has no audio content.", status=404)

@login_required    
def delete_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    
    if request.method == 'POST':
        # Delete the song
        song.delete()
        return redirect('dashboard')

    return render(request, '/home/sriharsha/django_frac_project/my_music/mymp3/templates/delete_song_confirm.html', {'song': song})
    
def logout_view(request):
    logout(request)
    # Redirect to the login page after logout
    return redirect('login')