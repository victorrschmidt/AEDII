from .Hashmap import Hashmap
from .Trie import Trie
import os

# Classe Searcher
class Searcher:
    def __init__(self, expected_key_amount: int):
        self.hashmap = Hashmap(expected_key_amount)
        self.trie = Trie()

    # Limpa o console
    def clear_console(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

    # Insere um corpo celeste no Searcher
    def insert(self, key: str, value: dict) -> None:
        self.hashmap.insert(key, value)
        self.trie.insert(key)

    # Remove um corpo celeste do Searcher
    def delete(self, key: str) -> None:
        if not key:
            return
        if self.hashmap.get(key) is not None:
            self.hashmap.delete(key)
            self.trie.delete(key)
            print(f"Corpo celeste {key} removido.")
        else:
            print(f"Corpo celeste {key} não encontrado.")

    # Mostra os corpos celestes que possuem o prefixo passado como parâmetro
    def filter(self, preffix: str) -> None:
        bodies = self.trie.get_words(preffix)
        if not bodies:
            print("Nenhum corpo celeste encontrado.")
            return
        print(f"Foram encontrados {len(bodies)} corpo(s) celeste(s):")
        for body in bodies:
            print(body)

    # Mostra as informações de um corpo celeste
    def search(self, name: str) -> None:
        body = self.hashmap.get(name)
        if body is None:
            print(f"Corpo celeste {name} não encontrado.")
            return
        body.debug()

    # Lê um inteiro no intervalo [mn, mx]
    def readint(self, mn: int, mx: int) -> int:
        while True:
            n = int(input())
            if mn <= n <= mx:
                return n
            print("Erro. Digite uma opção válida.")

    # Roda o programa
    def run(self) -> None:
        while True:
            print("Operações:")
            print("1 - Mostrar todos os corpos celestes")
            print("2 - Filtrar corpos celestes por prefixo")
            print("3 - Mostrar informações de corpo celeste")
            print("4 - Deletar corpo celeste")
            print("5 - Sair")
            option = self.readint(1, 5)
            self.clear_console()
            if option == 1:
                print("Corpos celestes:")
                for word in self.trie.get_all_words():
                    print(word)
            elif option == 2:
                preffix = input("Digite o prefixo do corpo celeste: ")
                self.filter(preffix)
            elif option == 3:
                name = input("Digite o nome do corpo celeste: ")
                self.search(name)
            elif option == 4:
                name = input("Digite o nome do corpo celeste: ")
                self.delete(name)
            else:
                break
        print("Encerrando o programa...")
