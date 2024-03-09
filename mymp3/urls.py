# mymp3/urls.py
from django.urls import path , include
from django.contrib.auth.views import LogoutView
from . import views
from .views import your_audio_view , logout_view , delete_song , home
from django.contrib.auth import views as auth_views
# from mymp3.registration import urls as registration_urls
# from .views import register_view, login_view, dashboard_view, upload_song_view


urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('home/', home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', logout_view, name='logout'),  # Add the 'logout' URL pattern
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('upload_song/', views.upload_song_view, name='upload_song'),
    path('audio/<int:song_id>/', your_audio_view, name='audio_view'),
    path('delete_song/<int:song_id>/', delete_song, name='delete_song'),
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

]
