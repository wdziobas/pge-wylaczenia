import requests
from bs4 import BeautifulSoup

URL = "https://pgedystrybucja.pl/wylaczenia/planowane-wylaczenia"
ULICA = "Łużycka"
MIASTO = "Łomianki"

def main():
    print("➡️ Start skryptu")
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(URL, headers=headers, timeout=30)
        print(f"✅ Status HTTP: {r.status_code}")
        r.raise_for_status()
    except Exception as e:
        print(f"❌ Błąd pobierania strony: {e}")
        return

    soup = BeautifulSoup(r.text, "html.parser")

    # Szukanie w HTML wszystkich elementów zawierających interesującą ulicę
    found = False
    for tag in soup.find_all(text=True):
        if ULICA in tag and MIASTO in tag:
            print("📢 ZNALEZIONO WYŁĄCZENIE:")
            print(tag.strip())
            found = True

    if not found:
        print("ℹ️ Brak planowa
