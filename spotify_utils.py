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

def get_available_genres(sp):
    token = sp.auth_manager.get_access_token(as_dict=False)
    url = "https://api.spotify.com/v1/recommendations/available-genre-seeds"
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    return resp.json().get("genres", [])
