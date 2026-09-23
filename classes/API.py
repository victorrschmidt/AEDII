import requests
import json

class API:
    URL = "https://api.le-systeme-solaire.net/rest/bodies"
    API_KEY = "c2245b58-5114-48e5-87a7-22d6bf6f25a5"
    HEADERS = {"Authorization": f"Bearer {API_KEY}"}

    @staticmethod
    def get_data():
        response = requests.get(API.URL, headers=API.HEADERS)
        if response.status_code != 200:
            raise Exception(f"Erro na API. Status: {response.status_code}")
        data = response.json()

        with open("bodies.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
