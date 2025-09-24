import requests

# Parametry wyszukiwania
params = {
    'miejscowosc': 'Łomianki',
    'ulica': 'Łużycka'
}

# Wysyłanie zapytania POST
response = requests.post('https://pgedystrybucja.pl/wylaczenia/planowane-wylaczenia', data=params)

if response.status_code == 200:
    data = response.json()
    if data['wyłączenia']:
        print("Planowane wyłączenia:")
        for item in data['wyłączenia']:
            print(f"Data: {item['data']}, Godzina: {item['godzina']}")
    else:
        print("Brak planowanych wyłączeń.")
else:
    print(f"Błąd pobierania danych: {response.status_code}")
