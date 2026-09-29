from .Searcher import Searcher
from .Huffman import Huffman
import json

# Classe Structs
class Structs:
    # Retorna um Searcher com os dados da API
    @staticmethod
    def searcher() -> Searcher:
        with open("bodies.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            body_count = len(data["bodies"])
            searcher = Searcher(body_count)
            for body in data["bodies"]:
                if body["id"].lower():
                    searcher.insert(body["id"].lower(), body)
            return searcher

    # Retorna um Huffman com os dados da API
    @staticmethod
    def huffman() -> Huffman:
        with open("bodies.json", "r", encoding="utf-8") as file:
            text = file.read()
            huffman = Huffman(text)
            return huffman
