import pandas as pd
import pycountry_convert as pc

# Charger le fichier d'origine
df = pd.read_csv("festivals_finals.csv")

# Garder uniquement les colonnes ville et pays
df_clean = df[['city', 'country']].drop_duplicates().dropna()

# Fonction pour obtenir le continent à partir du nom de pays
def get_continent(country_name):
    try:
        country_code = pc.country_name_to_country_alpha2(country_name)
        continent_code = pc.country_alpha2_to_continent_code(country_code)
        continent_name = {
            "AF": "Africa",
            "AS": "Asia",
            "EU": "Europe",
            "NA": "North America",
            "OC": "Oceania",
            "SA": "South America",
            "AN": "Antarctica"
        }
        return continent_name.get(continent_code, "Unknown")
    except Exception:
        return "Unknown"

# Appliquer la fonction pour créer la colonne "continent"
df_clean["continent"] = df_clean["country"].apply(get_continent)

# Exporter dans un nouveau CSV
df_clean.to_csv("cities_one.csv", index=False)
