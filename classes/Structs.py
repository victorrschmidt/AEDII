from .Hashmap import Hashmap
import json

class Structs:
    @staticmethod
    def hashmap_by_bodyname():
        with open("bodies.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            body_count = len(data["bodies"])
            hashmap = Hashmap(body_count)
            for body in data["bodies"]:
