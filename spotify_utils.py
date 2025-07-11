# spotify_utils.py

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI, SCOPE
import getpass

def get_spotify_client():
    print("▶️ Démarrage de l'authentification Spotify...")

    username = getpass.getuser()  # ← chaque utilisateur a un cache différent

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope=SCOPE,
        username=username,              # ← important pour identifier le cache
        cache_path=f".cache-{username}",# ← crée un fichier unique pour chaque utilisateur
        show_dialog=True                # ← force toujours la fenêtre d'autorisation
    ))

    print("✅ Authentification Spotify réussie.")
    return sp

def get_top_artists(sp, limit=20):
    results = sp.current_user_top_artists(limit=limit, time_range="long_term")
    artist_names = [artist["name"] for artist in results["items"]]
    print("\n🎧 Tes artistes les plus écoutés :")
    for name in artist_names:
        print(f" - {name}")
    return artist_names