from typing import Self

# Classe que contém um caracter e os nós filhos para serem inseridos na Trie
class Node:
    def __init__(self, char: str=None, parent: Self=None):
        self.char = char
        self.parent = parent
        self.is_final = False
        # 26 letras + 10 algarismos + hífen
        self.children = [None] * 37
        self.children_count = 0

# Classe Trie
class Trie:
    def __init__(self):
        self.log = []
        self.root = Node()
        self.size = 0
        self.node_count = 0
        self.visited_node_count = 0

    # Retorna todas as palavras contidas na Trie
    def get_all_words(self) -> list[str]:
        node = self.root
        stack = [(node, "")]
        word_list = []
        while stack:
            node, current_preffix = stack.pop()
            if node.is_final:
                word_list.append(current_preffix)
            for child in node.children:
                if child is not None:
                    stack.append((child, current_preffix + child.char))
        return sorted(word_list)

    # Mostra as informações da Trie
    def debug(self, show_logs: bool=True, show_words: bool=True) -> None:
        if show_logs:
            print("-------- Logs da Trie: --------")
            for log in self.log:
                print(log)
            print("-------- Fim dos Logs da Trie --------")
        if show_words:
            print("-------- Palavras contidas na Trie --------")
            for word in self.get_all_words():
                print(word)
            print("-------- Fim das Palavras da Trie --------")
        print("-------- Informações da Trie --------")
        print(f"Total de palavras armazenadas: {self.size}")
        print(f"Total de nós armazenados: {self.node_count}")
        print(f"Total de nós visitados: {self.visited_node_count}")
        print("-------- Fim do debug --------")

    # Registra uma operação efetuada na Trie
    def __register_log(self, text: str) -> None:
        log = f"Log {len(self.log) + 1}: {text}"
        self.log.append(log)

    # Retorna a posição de um caracter no array de filhos de um nó da Trie
    def __char_pos(self, char: str) -> int:
        if ord(char) >= ord('a'):
            return ord(char) - ord('a')
        elif ord(char) >= ord('0'):
            return ord(char) - ord('0') + 26
        else:
            return 36

    # Retorna uma lista de palavras contidas na Trie que possuem o prefixo passado como parâmetro
    def get_words(self, preffix: str) -> list[str]:
        node = self.root
        for char in preffix:
            pos = self.__char_pos(char)
            if node.children[pos] is None:
                self.__register_log(f"Busca: Buscou pelo prefixo '{preffix}' e não encontrou nenhuma palavra.")
                return []
            node = node.children[pos]
            self.visited_node_count += 1
        stack = [(node, preffix)]
        word_list = []
        while stack:
            node, current_preffix = stack.pop()
            if node.is_final:
                word_list.append(current_preffix)
            self.visited_node_count += 1
            for child in node.children:
                if child is not None:
                    stack.append((child, current_preffix + child.char))
        self.__register_log(f"Busca: Buscou pelo prefixo '{preffix}' e encontrou {len(word_list)} palavras.")
        return sorted(word_list)

    # Insere uma palavra na Trie
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            pos = self.__char_pos(char)
            if node.children[pos] is None:
                node.children[pos] = Node(char, node)
                node.children_count += 1
                self.node_count += 1
            node = node.children[pos]
            self.visited_node_count += 1
        if not node.is_final:
            node.is_final = True
            self.size += 1
            self.__register_log(f"Inserção: Inseriu a palavra '{word}' na Trie.")
        else:
            self.__register_log(f"Inserção: Tentou inserir a palavra '{word}' na Trie, mas ela já estava armazenada.")

    # Remove uma palavra da Trie (se existir)
    def delete(self, word: str) -> None:
        node = self.root
        for char in word:
            pos = self.__char_pos(char)
            if node.children[pos] is None:
                self.__register_log(f"Remoção: Tentou remover a palavra '{word}' da Trie, mas ela não existia.")
                return
            node = node.children[pos]
            self.visited_node_count += 1
        if not node.is_final:
            self.__register_log(f"Remoção: Tentou remover a palavra '{word}' da Trie, mas ela não existia.")
            return
        node.is_final = False
        self.size -= 1
        self.__register_log(f"Remoção: Removeu a palavra '{word}' da Trie.")
        if node.children_count > 0:
            return
        parent = node.parent
        char = node.char
        while parent is not None and not node.is_final:
            if node.children_count == 0:
                parent.children[self.__char_pos(char)] = None
                parent.children_count -= 1
                self.node_count -= 1
            else:
                break
            node = parent
            parent = node.parent
            char = node.char
