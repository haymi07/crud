# views.py
from django.shortcuts import render
from .models import Song, Genre
from django.contrib import messages
from django.db.models import Q

def index(request):
    songs = Song.objects.all()
    genres = Genre.objects.all()
    search_query = ""

    if request.method == "POST":
        if "create_song" in request.POST:
            song_name = request.POST.get("song_name")
            genre_id = request.POST.get("genre")
            genre = Genre.objects.get(id=genre_id)
            released_date = request.POST.get("released_date")
            artist = request.POST.get("artist")
            Song.objects.create(
                song_name=song_name,
                genre=genre,
                released_date=released_date,
                artist=artist
            )
            messages.success(request, "Song added successfully")

        elif "update_song" in request.POST:
            song_id = request.POST.get("id")
            song_name = request.POST.get("song_name")
            genre_id = request.POST.get("genre")
            genre = Genre.objects.get(id=genre_id)
            released_date = request.POST.get("released_date")
            artist = request.POST.get("artist")
            song = Song.objects.get(id=song_id)
            song.song_name = song_name
            song.genre = genre
            song.released_date = released_date
            song.artist = artist
            song.save()
            messages.success(request, "Song updated successfully")

        elif "delete_song" in request.POST:
            song_id = request.POST.get("id")
            Song.objects.get(id=song_id).delete()
            messages.success(request, "Song deleted successfully")

        elif "create_genre" in request.POST:
            genre_name = request.POST.get("genre_name")
            Genre.objects.create(
                name=genre_name
            )
            messages.success(request, "Genre added successfully")

        elif "update_genre" in request.POST:
            genre_id = request.POST.get("id")
            genre_name = request.POST.get("genre_name")
            genre = Genre.objects.get(id=genre_id)
            genre.name = genre_name
            genre.save()
            messages.success(request, "Genre updated successfully")

        elif "delete_genre" in request.POST:
            genre_id = request.POST.get("id")
            Genre.objects.get(id=genre_id).delete()
            messages.success(request, "Genre deleted successfully")

        elif "search" in request.POST:
            search_query = request.POST.get("query")
            songs = Song.objects.filter(
                Q(song_name__icontains=search_query) | 
                Q(genre__name__icontains=search_query) | 
                Q(released_date__icontains=search_query) | 
                Q(artist__icontains=search_query)
            )
            genres = Genre.objects.filter(
                Q(name__icontains=search_query)
            )

    context = {"songs": songs, "genres": genres, "search_query": search_query}
    return render(request, "index.html", context=context)
