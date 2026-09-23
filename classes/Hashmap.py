class Node:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next

class Hashmap:
    def __init__(self, expected_key_amount):
        self.log = []
        self.CAPACITY_FACTOR = 1.33
        self.capacity = int(expected_key_amount * self.CAPACITY_FACTOR) + 1
        self.table = [None for _ in range(self.capacity)]
        self.size = 0
        self.collision_count = 0

    # Retorna o numero hash para um chave
    def __hash(self, key):
        return hash(key) % self.capacity

    # Registra uma operacao efetuada no hashmap
    def __register_log(self, text):
        log = f"Log {len(self.log) + 1}: {text}"
        self.log.append(log)

    # Retorna o valor contido em uma chave do hashmap (ou None, se a chave nao existir)
    def get(self, key):
        chunk = self.__hash(key)
        node = self.table[chunk]
        while node != None:
            if node.key == key:
                self.__register_log(f"Busca: Encontrou a chave '{key}' no chunk {chunk} e retornou o valor {node.value}.")
                return node.value
            node = node.next
        self.__register_log(f"Busca: Nao encontrou a chave '{key}' no chunk {chunk}.")
        return None

    # Insere uma chave no hashmap (ou altera seu valor, se a chave ja existir)
    def insert(self, key, value):
        chunk = self.__hash(key)
        node = self.table[chunk]
        collision_count = 0
        while node != None:
            collision_count += 1
            if node.key == key:
                node.value = value
                self.__register_log(f"Inserção: Encontrou a chave '{key}' no chunk {chunk} e alterou seu valor para {value}.")
                return
            node = node.next
        node = Node(key, value, self.table[chunk])
        self.table[chunk] = node
        self.size += 1
        if collision_count > 0:
            self.collision_count += collision_count
            self.__register_log(f"Inserção: Nao encontrou a chave '{key}' no chunk {chunk} e a inseriu com valor {value}.\nHouve colisao. Total de colisoes: {self.collision_count}")
        else:
            self.__register_log(f"Inserção: Nao encontrou a chave '{key}' no chunk {chunk} e a inseriu com valor {value}.")

    # Deleta uma chave do hashmap, se a mesma existir
    def delete(self, key):
        chunk = self.__hash(key)
        node = self.table[chunk]
        if node == None:
            self.__register_log(f"Remoção: Nao encontrou a chave '{key}' no chunk {chunk}.")
            return
        if node.key == key:
            self.table[chunk] = self.table[chunk].next
            self.size -= 1
            self.__register_log(f"Remoção: Encontrou a chave '{key}' no chunk {chunk} e a deletou.")
            return
        prev = self.table[chunk]
        node = node.next
        while node != None:
            if node.key == key:
                prev.next = node.next
                self.size -= 1
                self.__register_log(f"Remoção: Encontrou a chave '{key}' no chunk {chunk} e a deletou.")
                return
            prev = node
            node = node.next
        self.__register_log(f"Remoção: Nao encontrou a chave '{key}' no chunk {chunk}.")
