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
from .models import FriendRequest, Playlist ,UserProfile, FriendRequest
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile


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

        # Get friend requests and playlists
        friend_requests = FriendRequest.objects.filter(to_user=request.user, accepted=False)
        playlists = Playlist.objects.filter(user=request.user)

        context = {
            'songs': songs,
            'friend_requests': friend_requests,
            'playlists': playlists,
        }

        return render(request, '/home/sriharsha/django_frac_project/my_music/mymp3/templates/dashboard.html', context)
    else:
        # Redirect to the login page if the user is not authenticated
        return redirect('login')
    # Check if the user is authenticated before filtering songs
    # if request.user.is_authenticated:
    #     user_id = request.user.id
    #     songs = Song.objects.filter(user_id=user_id)
    #     return render(request, '/home/sriharsha/django_frac_project/my_music/mymp3/templates/dashboard.html', {'songs': songs})
    # else:
    #     # Handle the case where the user is not authenticated (optional)
    #     # return render(request, '/home/sriharsha/django_frac_project/my_music/mymp3/templates/dashboard.html', {'songs': []})
    #     return redirect('login')

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

# def dashboard(request):
    # friend_requests = FriendRequest.objects.filter(to_user=request.user, accepted=False)
    # playlists = Playlist.objects.filter(user=request.user)

    # context = {
    #     'friend_requests': friend_requests,
    #     'playlists': playlists,
    # }

    # return render(request, '/home/sriharsha/django_frac_project/my_music/mymp3/templates/dashboard.html', context)




def send_playlist_request(request, friend_id):
    friend = get_object_or_404(UserProfile, id=friend_id)
    playlist = Playlist.objects.filter(user=friend.user).first()
    
    # Create logic to send playlist request
    # You may need to create a model for playlist requests similar to FriendRequest
    # The accepted attribute can be used to determine if the request is accepted or not

    return redirect('dashboard')

# def search_users(request):
#     if request.method == 'GET':
#         query = request.GET.get('q')
#         if query:
#             users = User.objects.filter(username__icontains=query).exclude(id=request.user.id)
#             return render(request, '/home/sriharsha/django_frac_project/my_music/mymp3/templates/search_users.html', {'users': users})
#     return render(request, '/home/sriharsha/django_frac_project/my_music/mymp3/templates/search_users.html', {'users': []})

# def search_users(request):
#     if request.method == 'GET':
#         query = request.GET.get('q', '')
#         users = User.objects.filter(username__icontains=query).values('username')
#         return JsonResponse(list(users), safe=False)
#     return JsonResponse([], safe=False)

def search_users(request):
    if request.method == 'GET':
        query = request.GET.get('q', '')
        users = User.objects.filter(username__icontains=query).values('username')
        return JsonResponse(list(users), safe=False)

    return JsonResponse([], safe=False)

# def send_friend_request(request, user_id):
#     if request.method == 'POST':
#         to_user = User.objects.get(id=user_id)
#         friend_request, created = FriendRequest.objects.get_or_create(
#             from_user=request.user,
#             to_user=to_user,
#             accepted=False
#         )
#         return redirect('search_users')  # Redirect to search page or any other page

# def send_friend_request(request):
#     if request.method == 'POST':
#         friend_username = request.POST.get('friend_username', '')
#         friend_user = User.objects.filter(username=friend_username).first()

#         if friend_user and friend_user != request.user:
#             # Check if a friend request already exists
#             existing_request = FriendRequest.objects.filter(from_user=request.user, to_user=friend_user).first()

#             if not existing_request:
#                 # Create a new friend request
#                 FriendRequest.objects.create(from_user=request.user, to_user=friend_user)

#     return redirect('dashboard')

@login_required
def send_friend_request(request):
    if request.method == 'POST':
        to_user_id = request.POST.get('to_user_id', '')
        to_user = get_object_or_404(User, id=to_user_id)

        # Check if a friend request already exists
        existing_request = FriendRequest.objects.filter(from_user=request.user, to_user=to_user, accepted=False).first()
        if existing_request:
            # Friend request already exists, handle accordingly (e.g., display a message)
            pass
        else:
            # Create a new friend request
            friend_request = FriendRequest(from_user=request.user, to_user=to_user)
            friend_request.save()

    return redirect('dashboard')

# def search_friends(request):
#     # Add your friend search logic here
#     # Retrieve the searched username from the GET parameters
#     search_username = request.GET.get('search_username', '')
#     # Implement the logic to search for friends based on the username

#     # For example:
#     found_friends = User.objects.filter(username__icontains=search_username)

#     return render(request, '/home/sriharsha/django_frac_project/my_music/mymp3/templates/search_friends.html', {'found_friends': found_friends})


def search_friends(request):
    if request.method == 'GET':
        search_username = request.GET.get('search_username', '')
        search_results = User.objects.filter(username__icontains=search_username).exclude(id=request.user.id)

    results_data = []
    for user in search_results:
        friend_request = FriendRequest.objects.filter(
            from_user=request.user,
            to_user=user,
            accepted=False
        ).first()

        results_data.append({
            'id': user.id,
            'username': user.username,
            'friend_request_sent': friend_request is not None,
            'friend_request_accepted': friend_request.accepted if friend_request else False,
        })

    return JsonResponse({'results': results_data})


# for accept friend

# def accept_friend_request(request, request_id):
#     friend_request = get_object_or_404(FriendRequest, id=request_id, to_user=request.user)
#     friend_request.accepted = True
#     friend_request.save()
#     # Add from_user to friends list
#     request.user.userprofile.friends.add(friend_request.from_user.userprofile)
#     return redirect('dashboard')

# def accept_friend_request(request, friend_request_id):
#     friend_request = FriendRequest.objects.filter(id=friend_request_id, to_user=request.user, accepted=False).first()

#     if friend_request:
#         # Accept the friend request
#         friend_request.accepted = True
#         friend_request.save()

#     return redirect('dashboard')

# @login_required
# def accept_friend_request(request, friend_request_id):
#     friend_request = FriendRequest.objects.get(pk=friend_request_id)

#     # Check if the current user is the receiver of the friend request
#     if request.user == friend_request.to_user:
#         friend_request.accept()
#         messages.success(request, f"You are now friends with {friend_request.from_user.username}.")
#         return redirect('dashboard')
#     else:
#         messages.error(request, "Invalid friend request.")
#         return redirect('dashboard')

# @login_required
# def accept_friend_request(request, friend_request_id):
#     friend_request = get_object_or_404(FriendRequest, id=friend_request_id)

#     # Check if the related objects exist before accessing them
#     if friend_request.from_user.userprofile:
#         # Access userprofile or perform any necessary actions
#         pass

#     if request.user == friend_request.to_user:
#         friend_request.accept()

#         # Add each other to friends list
#         request.user.userprofile.add_friend(friend_request.from_user)
#         friend_request.from_user.userprofile.add_friend(request.user)

#         messages.success(request, f"You are now friends with {friend_request.from_user.username}.")
#         return redirect('dashboard')
#     else:
#         messages.error(request, "Invalid friend request.")
#         return redirect('dashboard')
@login_required
def accept_friend_request(request, friend_request_id):
    friend_request = get_object_or_404(FriendRequest, id=friend_request_id)

    try:
        # Check if the related objects exist before accessing them
        to_user_profile = request.user.userprofile
        from_user_profile = friend_request.from_user.userprofile

        friend_request.accept()

        # Add each other to friends list
        to_user_profile.add_friend(friend_request.from_user)
        from_user_profile.add_friend(request.user)

        messages.success(request, f"You are now friends with {friend_request.from_user.username}.")
        return redirect('dashboard')

    except UserProfile.DoesNotExist:
        # Handle the case where UserProfile does not exist
        messages.error(request, "User profile does not exist.")
        return redirect('dashboard')

    except Exception as e:
        # Handle other exceptions
        messages.error(request, f"Error accepting friend request: {str(e)}")
        return redirect('dashboard')

def decline_friend_request(request, friend_request_id):
    friend_request = get_object_or_404(FriendRequest, id=friend_request_id)

    # Your logic to decline the friend request (mark it as declined, etc.)
    friend_request.decline()

    return redirect('dashboard')  # Redirect to the dashboard or any other appropriate page

def get_friends(request):
    user_profile = request.user.userprofile
    friends = user_profile.friends.all()

    friends_data = [{'id': friend.id, 'username': friend.user.username} for friend in friends]

    return JsonResponse({'friends': friends_data})


@login_required
def refresh_friends_list(request):
    user_profile = request.user.userprofile
    friends = user_profile.friends.all()

    # Assuming UserProfile has a field 'friends' representing the many-to-many relationship
    friends_list = [{'username': friend.user.username, 'id': friend.user.id} for friend in friends]

    return JsonResponse({'friends_list': friends_list})


def logout_view(request):
    logout(request)
    # Redirect to the login page after logout
    return redirect('login')


# yourappname/views.py
# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth import login, logout
# from .forms import SongForm
# from django.http import HttpResponse, JsonResponse
# from .models import Song, FriendRequest, Playlist, UserProfile
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# from django.contrib.auth.models import User
# from .models import UserProfile


# def home(request):
#     return render(request, 'home.html')


# def register_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('dashboard')
#     else:
#         form = UserCreationForm()

#     return render(request, '/home/sriharsha/django_frac_project/my_music/mymp3/templates/register.html', {'form': form, 'action': 'Register'})


# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('dashboard')
#     else:
#         form = AuthenticationForm()

#     return render(request, '/home/sriharsha/django_frac_project/my_music/mymp3/templates/login.html', {'form': form, 'action': 'Login'})


# # def dashboard_view(request):
# #     if request.user.is_authenticated:
# #         user_id = request.user.id
# #         songs = Song.objects.filter(user_id=user_id)

# #         friend_requests = FriendRequest.objects.filter(to_user=request.user, accepted=False)
# #         playlists = Playlist.objects.filter(user=request.user)

# #         context = {
# #             'songs': songs,
# #             'friend_requests': friend_requests,
# #             'playlists': playlists,
# #         }

# #         return render(request, 'dashboard.html', context)
# #     else:
# #         return redirect('login')

# # views.py
# @login_required
# def dashboard_view(request):
#     if request.user.is_authenticated:
#         user_id = request.user.id
#         songs = Song.objects.filter(user_id=user_id)

#     friend_requests = FriendRequest.objects.filter(to_user=request.user, accepted=False)
#     playlists = Playlist.objects.filter(user=request.user)

#     context = {
#         'songs': songs,
#         'friend_requests': friend_requests,
#         'playlists': playlists,
#     }

#     return render(request, '/home/sriharsha/django_frac_project/my_music/mymp3/templates/dashboard.html', context)

# def upload_song_view(request):
#     if request.method == 'POST':
#         form = SongForm(request.POST, request.FILES)
#         if form.is_valid():
#             song = form.save(commit=False)
#             song.user = request.user
#             song.save()
#             return redirect('dashboard')
#     else:
#         form = SongForm()
#     return render(request, '/home/sriharsha/django_frac_project/my_music/mymp3/templates/upload_song.html', {'form': form})


# def your_audio_view(request, song_id):
#     song = get_object_or_404(Song, id=song_id)

#     if song.audio_file_content:
#         response = HttpResponse(song.audio_file_content, content_type='audio/mp3')
#         response['Content-Disposition'] = f'inline; filename="{song.title}.mp3"'
#         return response
#     else:
#         return HttpResponse("Song not found or has no audio content.", status=404)


# @login_required
# def delete_song(request, song_id):
#     song = get_object_or_404(Song, id=song_id)

#     if request.method == 'POST':
#         song.delete()
#         return redirect('dashboard')

#     return render(request, '/home/sriharsha/django_frac_project/my_music/mymp3/templates/delete_song_confirm.html', {'song': song})


# def send_playlist_request(request, friend_id):
#     # Your logic for sending a playlist request
#     return redirect('dashboard')


# def search_users(request):
#     if request.method == 'GET':
#         query = request.GET.get('q', '')
#         users = User.objects.filter(username__icontains=query).values('username')
#         return JsonResponse(list(users), safe=False)

#     return JsonResponse([], safe=False)


# @login_required
# def send_friend_request(request):
#     if request.method == 'POST':
#         to_user_id = request.POST.get('to_user_id', '')
#         to_user = get_object_or_404(User, id=to_user_id)
#         pass

#         existing_request = FriendRequest.objects.filter(from_user=request.user, to_user=to_user, accepted=False).first()
#         if not existing_request:
#             friend_request = FriendRequest(from_user=request.user, to_user=to_user)
#             friend_request.save()

#     return redirect('dashboard')
# # @login_required
# # def send_friend_request(request, user_id):
# #     if request.method == 'POST':
# #         to_user = get_object_or_404(User, id=user_id)
        
# #         existing_request = FriendRequest.objects.filter(from_user=request.user, to_user=to_user, accepted=False).first()
# #         if not existing_request:
# #             friend_request = FriendRequest(from_user=request.user, to_user=to_user)
# #             friend_request.save()

# #     return redirect('dashboard')
# def search_friends(request):
#     if request.method == 'GET':
#         search_username = request.GET.get('search_username', '')
#         search_results = User.objects.filter(username__icontains=search_username).exclude(id=request.user.id)

#     results_data = []
#     for user in search_results:
#         friend_request = FriendRequest.objects.filter(
#             from_user=request.user,
#             to_user=user,
#             accepted=False
#         ).first()

#         results_data.append({
#             'id': user.id,
#             'username': user.username,
#             'friend_request_sent': friend_request is not None,
#             'friend_request_accepted': friend_request.accepted if friend_request else False,
#         })

#     return JsonResponse({'results': results_data})


# # @login_required
# # def accept_friend_request(request, friend_request_id):
# #     friend_request = get_object_or_404(FriendRequest, id=friend_request_id)

# #     try:
# #         to_user_profile = request.user.userprofile
# #         from_user_profile = friend_request.from_user.userprofile

# #         friend_request.accept()

# #         to_user_profile.add_friend(friend_request.from_user)
# #         from_user_profile.add_friend(request.user)

# #         messages.success(request, f"You are now friends with {friend_request.from_user.username}.")
# #         return redirect('dashboard')

# #     except UserProfile.DoesNotExist:
# #         messages.error(request, "User profile does not exist.")
# #         return redirect('dashboard')

# #     except Exception as e:
# #         messages.error(request, f"Error accepting friend request: {str(e)}")
# #         return redirect('dashboard')

# # @login_required
# # def accept_friend_request(request, friend_request_id):
# #     friend_request = get_object_or_404(FriendRequest, id=friend_request_id)

# #     try:
# #         # Check if the UserProfile exists for both users
# #         to_user_profile = request.user.userprofile
# #         from_user_profile = friend_request.from_user.userprofile

# #         if not to_user_profile or not from_user_profile:
# #             raise UserProfile.DoesNotExist("User profile does not exist.")

# #         friend_request.accept()

# #         # Add each other to friends list
# #         to_user_profile.add_friend(friend_request.from_user)
# #         from_user_profile.add_friend(request.user)

# #         messages.success(request, f"You are now friends with {friend_request.from_user.username}.")

# #         # Return a JSON response indicating success
# #         return JsonResponse({'success': True})

# #     except UserProfile.DoesNotExist as e:
# #         # Handle the case where UserProfile does not exist
# #         messages.error(request, str(e))
# #         return JsonResponse({'success': False, 'error': str(e)})

# #     except Exception as e:
# #         # Handle other exceptions
# #         messages.error(request, f"Error accepting friend request: {str(e)}")
# #         return JsonResponse({'success': False, 'error': str(e)})


# # @login_required
# # def accept_friend_request(request, friend_request_id):
# #     friend_request = get_object_or_404(FriendRequest, id=friend_request_id)

# #     try:
# #         # Check if the related objects exist before accessing them
# #         to_user_profile = request.user.userprofile
# #         from_user_profile = friend_request.from_user.userprofile

# #         friend_request.accept()

# #         # Add each other to friends list
# #         to_user_profile.add_friend(friend_request.from_user)
# #         from_user_profile.add_friend(request.user)

# #         messages.success(request, f"You are now friends with {friend_request.from_user.username}.")
# #         return redirect('dashboard')

# #     except UserProfile.DoesNotExist:
# #         # Handle the case where UserProfile does not exist
# #         messages.error(request, "User profile does not exist.")
# #         return redirect('dashboard')

# #     except Exception as e:
# #         # Handle other exceptions
# #         messages.error(request, f"Error accepting friend request: {str(e)}")
# #         return redirect('dashboard')

# # @login_required
# # def accept_friend_request(request, friend_request_id):
# #     friend_request = get_object_or_404(FriendRequest, id=friend_request_id, to_user=request.user)

# #     if friend_request:
# #         friend_request.accept()

# #         # Add each other to friends list
# #         request.user.userprofile.add_friend(friend_request.from_user)
# #         friend_request.from_user.userprofile.add_friend(request.user)

# #         messages.success(request, f"You are now friends with {friend_request.from_user.username}.")
# #         return redirect('dashboard')
# #     else:
# #         messages.error(request, "Invalid friend request.")
# #         return redirect('dashboard')

# @login_required
# def accept_friend_request(request, friend_request_id):
#     friend_request = get_object_or_404(FriendRequest, id=friend_request_id, to_user=request.user, accepted=False)
#     friend_request.accept()

#     response_data = {'success': True}
#     return JsonResponse(response_data)

# def decline_friend_request(request, friend_request_id):
#     friend_request = get_object_or_404(FriendRequest, id=friend_request_id)
#     friend_request.decline()

#     return redirect('dashboard')



# @login_required
# def refresh_friends_list(request):
#     friends = request.user.userprofile.friends.all()
#     return render(request, '/home/sriharsha/django_frac_project/my_music/mymp3/templates/refresh_friends_list.html', {'friends': friends})

# def logout_view(request):
#     logout(request)
#     return redirect('login')
