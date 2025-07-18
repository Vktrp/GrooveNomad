import pandas as pd

# 1. Charger les données
festivals_df = pd.read_csv("festivals_finals.csv")
destinations_df = pd.read_csv("Destinations.csv")

# 2. Normaliser les noms de ville et pays
def normalize(s):
    return str(s).strip().lower()

festivals_df["city_norm"] = festivals_df["city"].apply(normalize)
festivals_df["country_norm"] = festivals_df["country"].apply(normalize)
destinations_df["city_norm"] = destinations_df["city"].apply(normalize)
destinations_df["country_norm"] = destinations_df["country"].apply(normalize)

# 3. Supprimer les doublons dans Destinations
destinations_df = destinations_df.drop_duplicates(subset=["city_norm", "country_norm"])

# 4. Jointure
merged_df = pd.merge(
    festivals_df,
    destinations_df[["destination_id", "city_norm", "country_norm"]],
    on=["city_norm", "country_norm"],
    how="left"
)

# 5. Nettoyage
merged_df.drop(columns=["city_norm", "country_norm"], inplace=True)

# 6. Conversion de destination_id en entier (nullable)
merged_df["destination_id"] = merged_df["destination_id"].astype("Int64")

# 7. Sauvegarde
merged_df.to_csv("festivals_with_destination_id.csv", index=False)

print("✅ Fichier généré : festivals_with_destination_id.csv")
