
import requests
from bs4 import BeautifulSoup

URL = "https://pgedystrybucja.pl/strefa-klienta/planowane-wylaczenia"
ULICA = "Łużycka"
MIASTO = "Łomianki"

def main():
    r = requests.get(URL, timeout=20)
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "html.parser")

    # Zbierz wszystkie ogłoszenia
    entries = soup.find_all("div", class_="event-item")

    found = False
    for e in entries:
        text = e.get_text(" ", strip=True)
        if ULICA in text and MIASTO in text:
            print("📢 ZNALEZIONO WYŁĄCZENIE:")
            print(text)
            found = True
