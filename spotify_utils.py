# spotify_utils.py

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI, SCOPE
import getpass
from collections import Counter

def get_spotify_client():
    print("▶️ Démarrage de l'authentification Spotify...")

    username = getpass.getuser()  # ← chaque utilisateur a un cache différent

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope=SCOPE,
        username=username,
        cache_path=f".cache-{username}",
        show_dialog=True
    ))

    print("✅ Authentification Spotify réussie.")
    return sp

def get_top_artists(sp, limit=40):
    time_ranges = ["medium_term", "long_term"]
    artist_set = set()

    print("\n🎧 Tes artistes les plus écoutés :")

    for time_range in time_ranges:
        results = sp.current_user_top_artists(limit=limit, time_range=time_range)
        for artist in results["items"]:
            name = artist["name"]
            if name not in artist_set:
                artist_set.add(name)
                print(f" - {name}")

    return list(artist_set)

def get_user_top_genres(sp, limit=40, top_n=10):
    """Récupère les genres dominants à partir des artistes les plus écoutés, sans doublons"""
    time_ranges = ["medium_term", "long_term"]
    unique_artists = {}
    
    # Rassembler les artistes sans doublons
    for time_range in time_ranges:
        results = sp.current_user_top_artists(limit=limit, time_range=time_range)
        for artist in results["items"]:
            unique_artists[artist["id"]] = artist  # évite les doublons via ID Spotify

    # Compter les genres à partir des artistes uniques
    genres_counter = Counter()
    for artist in unique_artists.values():
        genres_counter.update(artist.get("genres", []))

    top_genres = genres_counter.most_common(top_n)

    print("\n🎼 Genres préférés de l'utilisateur (filtrés sans doublons artiste) :")
    for genre, count in top_genres:
        print(f" - {genre} ({count})")

    return [genre for genre, _ in top_genres]