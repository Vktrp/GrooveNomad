import requests
import pandas as pd
import json
import time

# Configuration
bing_api_key = "TA_CLE_API"  # remplace par ta clé
endpoint = "https://api.bing.microsoft.com/v7.0/search"
input_file = "festivals.csv"
output_file = "festivals_bing.csv"

headers = {"Ocp-Apim-Subscription-Key": bing_api_key}

def recherche_bing(query):
    params = {"q": query, "count": 5}
    try:
        response = requests.get(endpoint, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Erreur Bing API : {e}")
        return None

def extraire_info_descriptions(resultats):
    genre = "Inconnu"
    prix = "Inconnu"
    if not resultats:
        return genre, prix
    for result in resultats.get("webPages", {}).get("value", []):
        desc = result.get("snippet", "").lower()
        if any(g in desc for g in ["rock", "electro", "techno", "hip hop", "jazz", "reggae"]):
            genre = desc
        if any(p in desc for p in ["€", "eur", "euro", "$", "usd", "ticket", "price"]):
            prix = desc
        if genre != "Inconnu" and prix != "Inconnu":
            break
    return genre, prix

# Charger CSV
df = pd.read_csv(input_file)
genres = []
prix = []

for index, row in df.iterrows():
    nom = row.get("nom", "")
    lieu = row.get("lieu", "")
    dates = row.get("dates", "")
    requete = f"{nom} {lieu} {dates} genre musical ticket price site:festicket.com OR site:ticketmaster.com"
    print(f"🔎 Recherche : {requete}")
    
    resultats = recherche_bing(requete)
    genre, prix_estime = extraire_info_descriptions(resultats)

    genres.append(genre)
    prix.append(prix_estime)
    time.sleep(1)  # éviter de spammer l'API

# Ajout au DataFrame
df["genre_bing"] = genres
df["prix_bing"] = prix
df.to_csv(output_file, index=False)
print(f"✅ Données enrichies enregistrées dans : {output_file}")
