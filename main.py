# main.py

print("🚀 Script lancé")

import pandas as pd
from spotify_utils import get_spotify_client, get_top_artists
from ticketmaster_utils import search_events_for_artists

# 1. Authentification Spotify
sp = get_spotify_client()

# 2. Récupération des artistes
artist_names = get_top_artists(sp)

# 3. Recherche des événements
all_events = search_events_for_artists(artist_names)

# 4. Résultats
if all_events:
    df = pd.DataFrame(all_events)
    print("\n🎫 Événements trouvés :")
    print(df.to_string(index=False))

    # Export CSV
    df.to_csv("concerts_resultats.csv", index=False, encoding="utf-8")
    print("📁 Résultats exportés dans 'concerts_resultats.csv'")
else:
    print("\n❌ Aucun événement trouvé.")

from clear_cache import clear_spotify_cache

# 5. Nettoyage final
clear_spotify_cache()
