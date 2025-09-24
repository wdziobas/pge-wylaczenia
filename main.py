import requests
from bs4 import BeautifulSoup

URL = "https://pgedystrybucja.pl/strefa-klienta/planowane-wylaczenia"
ULICA = "Łużycka"
MIASTO = "Łomianki"

def main():
    print("➡️ Start skryptu")
    try:
        r = requests.get(URL, timeout=30)
        print(f"✅ Status HTTP: {r.status_code}")
        r.raise_for_status()
    except Exception as e:
        print(f"❌ Błąd pobierania strony: {e}")
        return

    html = r.text
    print("🔹 Początek pobranej strony (500 znaków):")
    print(html[:500])
    print("------ KONIEC FRAGMENTU ------")

    soup = BeautifulSoup(html, "html.parser")

    # diagnostyka - pokażmy nagłówki
    headers = [h.get_text(" ", strip=True) for h in soup.find_all(["h1", "h2", "h3", "h4"])]
    print("🔎 Nagłówki znalezione na stronie:", headers)

    # właściwe szukanie wyłączeń
    entries = soup.find_all("div")
    found = False
    for e in entries:
        text = e.get_text(" ", strip=True)
        if ULICA in text and MIASTO in text:
            print("📢 ZNALEZIONO WYŁĄCZENIE:")
            print(text)
            found = True

    if not found:
        print("ℹ️ Brak planowanych wyłączeń na ul. Łużyckiej w Łomiankach.")

if __name__ == "__main__":
    main()
