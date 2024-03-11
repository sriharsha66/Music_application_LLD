# mymp3/urls.py
from django.urls import path , include
from django.contrib.auth.views import LogoutView
from . import views
from .views import your_audio_view , logout_view , delete_song , home
from django.contrib.auth import views as auth_views
# from mymp3.registration import urls as registration_urls
from .views import accept_friend_request, send_playlist_request ,search_users, send_friend_request ,get_friends ,refresh_friends_list


urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('home/', home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', logout_view, name='logout'),  # Add the 'logout' URL pattern
    path('dashboard/', views.dashboard_view, name='dashboard'),
    # path('dashboard/', dashboard, name='dashboard'),
    path('upload_song/', views.upload_song_view, name='upload_song'),
    path('audio/<int:song_id>/', your_audio_view, name='audio_view'),
    path('delete_song/<int:song_id>/', delete_song, name='delete_song'),
    path('accept_friend_request/<int:friend_request_id>/', accept_friend_request, name='accept_friend_request'),
    path('send_playlist_request/<int:friend_id>/', send_playlist_request, name='send_playlist_request'),
    path('search_users/', search_users, name='search_users'),
    path('send_friend_request/<int:user_id>/', send_friend_request, name='send_friend_request'),
    path('search-friends/', views.search_friends, name='search_friends'),
    path('send_friend_request/', send_friend_request, name='send_friend_request'),
    path('get_friends/', get_friends, name='get_friends'),
    path('refresh_friends_list/', get_friends, name='refresh_friends_list'),

]
    # path('', include('mymp3.registration.urls')),  # Include the registration URLs

    # path('', include(registration_urls)),
    # path('register/', register_view, name='register'),
    # path('login/', login_view, name='login'),
    # path('dashboard/', dashboard_view, name='dashboard'),
    # path('upload_song/', upload_song_view, name='upload_song'),

    # Add other URL patterns as needed

     # Password Reset URLs
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),



# mymp3/urls.py
# from django.urls import path
# from . import views
# from .views import your_audio_view, logout_view, delete_song, home, accept_friend_request, send_playlist_request, search_users, send_friend_request ,refresh_friends_list

# urlpatterns = [
#     path('register/', views.register_view, name='register'),
#     path('home/', home, name='home'),
#     path('login/', views.login_view, name='login'),
#     path('logout/', logout_view, name='logout'),
#     path('dashboard/', views.dashboard_view, name='dashboard'),
#     path('upload_song/', views.upload_song_view, name='upload_song'),
#     path('audio/<int:song_id>/', your_audio_view, name='audio_view'),
#     path('delete_song/<int:song_id>/', delete_song, name='delete_song'),
#     path('accept_friend_request/<int:friend_request_id>/', accept_friend_request, name='accept_friend_request'),
#     path('send_playlist_request/<int:friend_id>/', send_playlist_request, name='send_playlist_request'),
#     path('search_users/', search_users, name='search_users'),
#     # path('send_friend_request/<int:user_id>/', send_friend_request, name='send_friend_request'),
#     path('send_friend_request/<int:user_id>/', views.send_friend_request, name='send_friend_request'),
#     path('search-friends/', views.search_friends, name='search_friends'),
#     path('refresh-friends-list/', refresh_friends_list, name='refresh_friends_list'),

#     # Choose one of the paths below based on your requirements
#     # path('send_friend_request/', views.send_friend_request, name='send_friend_request'),
#     # path('send_friend_request/', send_friend_request, name='send_friend_request_param'),  # If you need a parameter ]

