# admin.py
from django.contrib import admin
from .models import Song, Genre

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ["id", "song_name", "genre", "released_date", "artist"]
