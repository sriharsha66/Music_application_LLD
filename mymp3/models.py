# # yourappname/models.py
# from django.db import models
# from django.contrib.auth.models import User

# class Song(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     audio_file = models.FileField(upload_to='audio/')
#     audio_file_content = models.BinaryField(null=True, blank=True)

#     def save(self, *args, **kwargs):
#         # Read the audio file content and save it to the database
#         if self.audio_file:
#             self.audio_file_content = self.audio_file.read()
#             self.audio_file.seek(0)
#         super().save(*args, **kwargs)
# # models.py
# from django.contrib.auth.models import User

# # class UserProfile(models.Model):
# #     user = models.OneToOneField(User, on_delete=models.CASCADE)
# #     friends = models.ManyToManyField('self', symmetrical=False, blank=True)
# # models.py
# class Playlist(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#     songs = models.ManyToManyField(Song)
# # models.py
# # class FriendRequest(models.Model):
# #     from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
# #     to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)
# #     accepted = models.BooleanField(default=False)

# #     def __str__(self):
# #         return f'{self.from_user.username} to {self.to_user.username} ({self.accepted})'

# class UserProfile(models.Model):
#     # Your UserProfile model fields go here
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # Add other fields as needed

# # 1:47am added
# class FriendRequest(models.Model):
#     from_user = models.ForeignKey(User, related_name='sent_requests', on_delete=models.CASCADE)
#     to_user = models.ForeignKey(User, related_name='received_requests', on_delete=models.CASCADE)
#     accepted = models.BooleanField(default=False)

#     def accept(self):
#         self.accepted = True
#         self.save()


# yourappname/models.py
from django.db import models
from django.contrib.auth.models import User

class Song(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='audio/')
    audio_file_content = models.BinaryField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Read the audio file content and save it to the database
        if self.audio_file:
            self.audio_file_content = self.audio_file.read()
            self.audio_file.seek(0)
        super().save(*args, **kwargs)

class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    songs = models.ManyToManyField(Song)

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # Add other fields as needed

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField('self', symmetrical=False, blank=True)

    def add_friend(self, friend):
        self.friends.add(friend)

class FriendRequest(models.Model):
    from_user = models.ForeignKey(User, related_name='sent_requests', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='received_requests', on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)

    def accept(self):
        self.accepted = True
        self.save()
