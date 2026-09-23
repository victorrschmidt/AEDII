import json
from urllib.request import Request, urlopen

class API:
    # Informações da API
    URL = "https://api.le-systeme-solaire.net/rest/bodies"
    API_KEY = "c2245b58-5114-48e5-87a7-22d6bf6f25a5"
    HEADERS = {"Authorization": f"Bearer {API_KEY}"}

    # Resgata os dados da API
    @staticmethod
    def get_data():
        request = Request(API.URL, headers=API.HEADERS)

        with urlopen(request) as response:
            if response.status != 200:
                raise Exception(f"Erro na API. Status: {response.status}")
            data = json.load(response)

        with open("bodies.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
