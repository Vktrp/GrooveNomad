# ticketmaster_utils.py

import requests
import time
from config import TICKETMASTER_API_KEY

def search_events_for_artists(artist_names):
    all_events = []

    for artist_name in artist_names:
        print(f"\n🔍 Recherche de concerts pour : {artist_name}")
        search_url = "https://app.ticketmaster.com/discovery/v2/attractions.json"
        params = {
            "apikey": TICKETMASTER_API_KEY,
            "keyword": artist_name
        }
        r = requests.get(search_url, params=params)
        data = r.json()

        if "_embedded" not in data:
            print("   ⚠️ Aucun résultat.")
            continue

        attraction_id = data["_embedded"]["attractions"][0]["id"]

        events_url = "https://app.ticketmaster.com/discovery/v2/events.json"
        params = {
            "apikey": TICKETMASTER_API_KEY,
            "attractionId": attraction_id,
            "size": 50
        }
        r_events = requests.get(events_url, params=params)
        data_events = r_events.json()

        if "_embedded" not in data_events:
            print("   ❌ Aucun événement trouvé.")
            continue

        for event in data_events["_embedded"]["events"]:
            venue = event.get("_embedded", {}).get("venues", [{}])[0]
            all_events.append({
                "artist": artist_name,
                "event": event.get("name"),
                "date": event.get("dates", {}).get("start", {}).get("localDate"),
                "time": event.get("dates", {}).get("start", {}).get("localTime"),
                "venue": venue.get("name", ""),
                "city": venue.get("city", {}).get("name", ""),
                "country": venue.get("country", {}).get("name", ""),
                "url": event.get("url", "")
            })

        time.sleep(0.5)

    return all_events