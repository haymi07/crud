# models.py
from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name="Genre Name")

    def __str__(self):
        return str(self.id)

class Song(models.Model):
    song_name = models.CharField(max_length=100, verbose_name="Song Name")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name="Genre")
    released_date = models.DateField(verbose_name="Released Date")
    artist = models.CharField(max_length=100, verbose_name="Artist")

    def __str__(self):
        return str(self.id)
