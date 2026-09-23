from .Hashmap import Hashmap
import json

class Structs:
    # Cria um Hashmap onde a chave é o nome do corpo
    # e o valor são as informações do mesmo.
    @staticmethod
    def hashmap_by_bodyname():
        with open("bodies.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            body_count = len(data["bodies"])
            hashmap = Hashmap(body_count)
            for body in data["bodies"]:
                if body["englishName"]:
                    hashmap.insert(body["englishName"], body)
            return hashmap
