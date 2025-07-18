import pandas as pd
import time
import google.generativeai as genai
 
# === Configuration Gemini ===
genai.configure(api_key="AIzaSyBvxoPLxuctwm0Ylo7Cp0E-2JW1ypHM0U4")
model = genai.GenerativeModel("gemini-2.0-flash")
 
# === Chargement du fichier contenant les noms des festivals ===
df = pd.read_csv("festivals.csv")
 
# Vérifie qu’il y a une colonne "Nom"
if "nom" not in df.columns:
    raise ValueError("Le fichier CSV doit contenir une colonne 'nom'.")
 
# Liste pour stocker les genres récupérés
prix_list = []
 
# === Boucle sur chaque nom de festival ===
for i, nom in enumerate(df["nom"]):
    prompt = (
        "Tu es un expert en musique. Pour chaque nom de festival, donne le prix minumum et le prix maximum en une ligne, sans explication.\n"
        "Format attendu : juste les prix, séparés par des virgules si nécessaire.\n"
        "Exemples :\n"
        " - VERMONT BREWERS FESTIVAL 2025 → 60 USD, 65 USD\n"
        " - SUN & THUNDER FESTIVAL 2025 → 180 €, 180 €\n"
        " - SUPER BOCK SUPER ROCK 2025 → N/A Annulé, N/A Annulé\n"
        " - ATLAS WEEKEND 2025 → 1 800 UAH, 3 500 UAH\n"
        f"\nFestival : {nom}\nPrix :"
    )
 
    try:
        response = model.generate_content(prompt)
        prix = response.text.strip()

    except Exception as e:
        prix = "Erreur"
        print(f"Erreur sur {nom} → {e}")
 
    prix_list.append(prix)
    print(f"[{i+1}/{len(df)}] {nom} → {prix}")
    time.sleep(4.1)  # Respecte la limite de 15 requêtes/minute
 
# Ajoute la nouvelle colonne au DataFrame
df["prix"] = prix_list
 
# Sauvegarde dans un nouveau CSV
df.to_csv("festivals_prix.csv", index=False, encoding="utf-8")
print("✅ CSV généré : festivals_prix.csv")