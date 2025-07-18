import pandas as pd
from datetime import datetime

# Charger le CSV
df = pd.read_csv("festivals.csv")

# Fonction robuste pour parser les dates
def parse_festival_dates(date_str):
    if pd.isna(date_str) or "Cancelled" in date_str:
        return "Cancelled", "Cancelled"

    date_str = str(date_str).replace("–", "-").replace("  ", " ").strip()
    
    try:
        if "-" in date_str:
            # Cas avec deux mois différents : "July 31- August 1, 2026"
            if any(month in date_str for month in [
                "January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"
            ]) and date_str.count("-") == 1 and any(m in date_str.split("-")[1] for m in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]):
                range_part, year = date_str.rsplit(",", 1)
                month_day_start, month_day_end = range_part.split("-")
                month1, day1 = month_day_start.strip().split()
                month2, day2 = month_day_end.strip().split()
                year = year.strip()
                start = datetime.strptime(f"{month1} {day1} {year}", "%B %d %Y").strftime("%Y-%m-%d")
                end = datetime.strptime(f"{month2} {day2} {year}", "%B %d %Y").strftime("%Y-%m-%d")
                return start, end

            # Cas classique "July 17-19, 2025"
            date_str = date_str.replace("- ", "-").replace(" -", "-")
            range_part, year = date_str.rsplit(",", 1)
            parts = range_part.strip().split()
            month = parts[0]
            days = parts[1]
            start_day, end_day = days.split("-")
            start = datetime.strptime(f"{month} {start_day} {year.strip()}", "%B %d %Y").strftime("%Y-%m-%d")
            end = datetime.strptime(f"{month} {end_day} {year.strip()}", "%B %d %Y").strftime("%Y-%m-%d")
            return start, end
        else:
            # Cas unique : "July 20, 2025"
            date = datetime.strptime(date_str, "%B %d, %Y").strftime("%Y-%m-%d")
            return date, date
    except Exception:
        return "Invalid", "Invalid"

# Appliquer la fonction uniquement à la colonne 'dates'
df[['start_date', 'end_date']] = df['dates'].apply(lambda x: pd.Series(parse_festival_dates(x)))

# Sauvegarder le fichier propre
df.to_csv("festivals_datesSplited.csv", index=False)

print("✅ Dates correctement parsées. Fichier sauvegardé sous 'festivals_cleaned.csv'.")
