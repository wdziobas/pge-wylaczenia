import requests
from bs4 import BeautifulSoup
from datetime import datetime

URL = "https://pgedystrybucja.pl/wylaczenia/planowane-wylaczenia"
ULICA = "Łużycka"
MIASTO = "Łomianki"
RAPORT = "raport.txt"

def main():
    raport_lines = []
    raport_lines.append(f"➡️ Start skryptu: {datetime.now()}")

    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        r = requests.get(URL, headers=headers, timeout=30)
        r.raise_for_status()
        raport_lines.append(f"✅ Status HTTP: {r.status_code}")
    except Exception as e:
        raport_lines.append(f"❌ Błąd pobierania strony: {e}")
        zapis_raportu(raport_lines)
        return

    soup = BeautifulSoup(r.text, "html.parser")

    found = False
    # uzywamy string zamiast text, aby uniknąć DeprecationWarning
    for tag in soup.find_all(string=True):
        if ULICA in tag and MIASTO in tag:
            raport_lines.append("📢 ZNALEZIONO WYŁĄCZENIE:")
            raport_lines.append(tag.strip())
            found = True

    if not found:
        raport_lines.append("ℹ️ Brak planowanych wyłączeń na ul. Łużyckiej w Łomiankach.")

    zapis_raportu(raport_lines)

def zapis_raportu(lines):
    with open(RAPORT, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")
    print(f"✅ Raport zapisany do {RAPORT}")

if __name__ == "__main__":
    main()
