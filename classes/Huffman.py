from typing import Self, Any
from heapq import heappush, heappop

# Classe que contém uma chave e os campos para serem armazenados no MiniHashmap
class MiniNode:
    def __init__(self, key: str, value: Any, next: Self):
        self.key = key
        self.value = value
        self.next = next

# Classe MiniHashmap (específico para a árvore de Huffman)
class MiniHashmap:
    def __init__(self):
        self.capacity = 142
        self.table = [None] * self.capacity

    # Retorna o número hash para uma chave
    def __hash(self, key: str) -> int:
        return hash(key) % self.capacity

    # Retorna a frequência de um caracter
    def get(self, key: str) -> MiniNode:
        chunk = self.__hash(key)
        node = self.table[chunk]
        while node is not None:
            if node.key == key:
                return node
            node = node.next
        return None

    # Insere uma chave no MiniHashmap
    def insert(self, key: str, value: Any) -> None:
        chunk = self.__hash(key)
        node = MiniNode(key, value, self.table[chunk])
        self.table[chunk] = node

# Classe que contém um nó da árvore de Huffman
class Node:
    def __init__(self, char: str=None, frequency: int=0, left: Self=None, right: Self=None):
        self.char = char
        self.frequency = frequency
        self.left = left
        self.right = right

    # Comparador para ser usado no heap
    def __lt__(self, other: Self) -> bool:
        if self.frequency != other.frequency:
            return self.frequency < other.frequency
        if self.char is None:
            return True
        return False

# Classe Huffman
class Huffman:
    def __init__(self, text: str):
        self.root = Node()
        self.text = text

    # Constrói a árvore de Huffman
    def __build_tree(self) -> None:
        frequency_table = MiniHashmap()
        for char in self.text:
            node = frequency_table.get(char)
            if node is not None:
                node.value += 1
            else:
                frequency_table.insert(char, 1)
        pairs = []
        for node in frequency_table.table:
            while node is not None:
                pairs.append(Node(node.key, node.value))
                node = node.next
        heap = []
        for pair in pairs:
            heappush(heap, pair)
        while len(heap) > 1:
            lnode = heappop(heap)
            rnode = heappop(heap)
            new_node = Node(None, lnode.frequency + rnode.frequency, lnode, rnode)
            heappush(heap, new_node)
        self.root = heappop(heap)

    # Verifica a tabela de frequências para cada caracter da mensagem
    def __get_frequency_table(self) -> None:
        frequency_table = MiniHashmap()
        stack = [(self.root, "")]
        while stack:
            node, current_preffix = stack.pop()
            if node.char is not None:
                frequency_table.insert(node.char, current_preffix)
            if node.left is not None:
                stack.append((node.left, current_preffix + "0"))
            if node.right is not None:
                stack.append((node.right, current_preffix + "1"))
        frequency_table_list = []
        for node in frequency_table.table:
            while node is not None:
                frequency_table_list.append((node.key, node.value))
                node = node.next
        frequency_table_list.sort(key=lambda pair: (len(pair[1]), pair[1]))
        table_text = "Caracter | Código\n"
        for char, code in frequency_table_list:
            char = char if char != '\n' else "\\n"
            table_text += f"| {char} | {code}\n"
        table_text += "\nAPI codificada:\n"
        bit_count = 0
        for char in self.text:
            code = frequency_table.get(char).value
            table_text += code
            bit_count += len(code)
        table_text += f"\n\nBits: {bit_count}\n"
        with open("codificacao.txt", "w", encoding="utf-8") as file:
            file.write(table_text)

    # Codifica o texto
    def encode(self) -> None:
        self.__build_tree()
        self.__get_frequency_table()
