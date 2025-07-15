# main.py

print("🚀 Script lancé")

import pandas as pd
from spotify_utils import get_spotify_client, get_top_artists, get_available_genres
from ticketmaster_utils import search_events_for_artists
from clear_cache import clear_spotify_cache

# 1. Authentification Spotify
sp = get_spotify_client()

# Genres disponibles sur Spotify
genres = get_available_genres(sp)
print("\n🎼 Genres Spotify disponibles :")
for g in genres:
    print(f" - {g}")

# 2. Récupération des artistes
artist_names = get_top_artists(sp)

# 3. Recherche des événements
all_events = search_events_for_artists(artist_names)

# 4. Résultats
if all_events:
    df = pd.DataFrame(all_events)

    print("\n🎫 Événements trouvés (avant filtrage) :")
    print(df.to_string(index=False))

    # 🎯 Filtrage : retirer les événements où le nom de l’artiste apparaît dans le nom de l’événement
    df_filtered = df[~df.apply(lambda row: row["artist"].lower() in row["event"].lower(), axis=1)]

    print("\n🧹 Événements après suppression des doublons nom_artist ↔ nom_event :")
    print(df_filtered.to_string(index=False))

    # 🔁 Supprimer les doublons (même artiste, même date → une seule ligne)
    df_filtered = df_filtered.drop_duplicates(subset=["artist", "date"], keep="first")

    # 📁 Export CSV
    df_filtered.to_csv("concerts_resultats.csv", index=False, encoding="utf-8")
    print("\n📁 Résultats exportés dans 'concerts_resultats.csv'")
else:
    print("\n❌ Aucun événement trouvé.")

# 5. Nettoyage du cache Spotify
clear_spotify_cache()