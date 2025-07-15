# main.py

print("🚀 Script lancé")

import pandas as pd
from spotify_utils import get_spotify_client, get_top_artists, get_user_top_genres
from clear_cache import clear_spotify_cache

# 1. Authentification Spotify
sp = get_spotify_client()

# Genres disponibles sur Spotify
user_genres = get_user_top_genres(sp)
print("\n🎯 Genres musicaux préférés de l'utilisateur :")
for g in user_genres:
    print(f" - {g}")

# 2. Récupération des artistes
artist_names = get_top_artists(sp)

# 5. Nettoyage du cache Spotify
clear_spotify_cache()