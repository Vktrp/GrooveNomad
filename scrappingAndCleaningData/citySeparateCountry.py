import pandas as pd

# Chargement du CSV
df = pd.read_csv("festivals_finals.csv")

# Suppression des espaces en début/fin et séparation
df[['city', 'country']] = df['lieu'].str.strip().str.rsplit(',', n=1, expand=True)

# Suppression des espaces restants
df['city'] = df['city'].str.strip()
df['country'] = df['country'].str.strip()

# Vérification
print(df[['lieu', 'city', 'country']].head())

# Optionnel : sauvegarder dans un nouveau fichier
df.to_csv("festivals_separes.csv", index=False)
