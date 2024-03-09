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
