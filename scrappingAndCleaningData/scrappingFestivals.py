import time
import csv
import undetected_chromedriver as uc  
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Configuration navigateur (sans headless pour éviter Cloudflare)
driver = uc.Chrome(headless=False)

# Génère toutes les URLs de page
pages = ["https://www.musicfestivalwizard.com/all-festivals/"] + [
    f"https://www.musicfestivalwizard.com/all-festivals/page/{i}/" for i in range(2, 54 )
]

festivals = []

for url in pages:
    driver.get(url)
    print(f"🔄 Chargement : {url}")
    time.sleep(5)  # attendre que la page JS soit chargée

    cards = driver.find_elements(By.CLASS_NAME, "entry-title")
    print(f"🎵 Festivals trouvés sur la page : {len(cards)}")

    for card in cards:
        try:
            nom = card.find_element(By.TAG_NAME, "h2").text.strip()
            lien = card.find_element(By.TAG_NAME, "a").get_attribute("href")

            meta = card.find_element(By.CLASS_NAME, "search-meta").get_attribute("innerHTML")
            meta_parts = meta.strip().split("<br>")
            lieu = meta_parts[0].strip()
            dates = meta_parts[1].split("/")[0].strip() if len(meta_parts) > 1 else ""

            festivals.append({
                "nom": nom,
                "dates": dates,
                "lieu": lieu
            })
        except NoSuchElementException:
            continue

    time.sleep(2)

driver.quit()

# Export CSV
with open("festivals.csv", "w", newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=["nom", "dates", "lieu"])
    writer.writeheader()
    writer.writerows(festivals)

print(f"\n✅ Total festivals récupérés : {len(festivals)} festivals enregistrés dans festivals_complet.csv")
