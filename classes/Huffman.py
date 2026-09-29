from typing import Self
from heapq import heappush, heappop

# Classe que contém um nó da árvore de Huffman
class Node:
    def __init__(self, char: str=None, frequency: int=0, left: Self=None, right: Self=None):
        self.char = char
        self.frequency = frequency
        self.left = left
        self.right = right

    # Comparador para ser usado no heap
    def __lt__(self, other: Self):
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
        frequency_table = dict()
        for char in self.text:
            if char in frequency_table:
                frequency_table[char] += 1
            else:
                frequency_table[char] = 1
        pairs = [Node(char, frequency) for char, frequency in frequency_table.items()]
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
        frequency_table = dict()
        stack = [(self.root, "")]
        while stack:
            node, current_preffix = stack.pop()
            if node.char is not None:
                frequency_table[node.char] = current_preffix
            if node.left is not None:
                stack.append((node.left, current_preffix + "0"))
            if node.right is not None:
                stack.append((node.right, current_preffix + "1"))
        frequency_table_list = [(char, code) for char, code in frequency_table.items()]
        frequency_table_list.sort(key=lambda pair: (len(pair[1]), pair[1]))
        table_text = "Caracter | Código\n"
        for char, code in frequency_table_list:
            char = char if char != '\n' else "\\n"
            table_text += f"| {char} | {code}\n"
        table_text += "\nAPI codificada:\n"
        bit_count = 0
        for char in self.text:
            table_text += frequency_table[char]
            bit_count += len(frequency_table[char])
        table_text += f"\n\nBits: {bit_count}"
        with open("codificacao.txt", "w", encoding="utf-8") as file:
            file.write(table_text)

    # Codifica o texto
    def encode(self) -> None:
        self.__build_tree()
        self.__get_frequency_table()
