# clear_cache.py

import os
import glob

def clear_spotify_cache():
    cache_files = glob.glob(".cache*")
    if not cache_files:
        print("🧼 Aucun fichier de cache à supprimer.")
    else:
        for file in cache_files:
            try:
                os.remove(file)
                print(f"🧹 Supprimé : {file}")
            except Exception as e:
                print(f"⚠️ Erreur lors de la suppression de {file} : {e}")