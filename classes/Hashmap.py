# Classe que contém uma chave e um valor para ser armazenado no Hashmap
class Node:
    def __init__(self, key, value, next):
        self.key = key
        self.value = value
        self.next = next

# Classe Hashmap
class Hashmap:
    def __init__(self, expected_key_amount):
        self.log = []
        self.CAPACITY_FACTOR = 1.42
        self.capacity = int(expected_key_amount * self.CAPACITY_FACTOR) + 1
        self.table = [None] * self.capacity
        self.used_chunk = [False] * self.capacity
        self.used_chunk_count = 0
        self.size = 0
        self.collision_count = 0

    # Mostra as informações do Hashmap
    def debug(self, show_logs=True):
        if show_logs:
            print("Logs do Hashmap:")
            for log in self.log:
                print(log)
        print("--- Informações do Hashmap ---")
        print(f"Total de chaves armazenadas: {self.size}")
        print(f"Total de chunks na tabela: {self.capacity}")
        print(f"Total de chunks utilizados: {self.used_chunk_count}")
        print(f"Total de colisões: {self.collision_count}")
        print("--- Fim do debug ---")

    # Retorna o número hash para uma chave
    def __hash(self, key):
        return hash(key) % self.capacity

    # Registra uma operação efetuada no Hashmap
    def __register_log(self, text):
        log = f"Log {len(self.log) + 1}: {text}"
        self.log.append(log)

    # Retorna o valor contido em uma chave do Hashmap (ou None, se a chave não existir)
    def get(self, key):
        chunk = self.__hash(key)
        node = self.table[chunk]
        while node != None:
            if node.key == key:
                self.__register_log(f"Busca: Encontrou a chave '{key}' no chunk {chunk} e retornou o valor.")
                return node.value
            node = node.next
        self.__register_log(f"Busca: Nao encontrou a chave '{key}' no chunk {chunk}.")
        return None

    # Insere uma chave no Hashmap (ou altera seu valor, se a chave já existir)
    def insert(self, key, value):
        chunk = self.__hash(key)
        node = self.table[chunk]
        collision_count = 0
        while node != None:
            collision_count += 1
            if node.key == key:
                node.value = value
                self.__register_log(f"Inserção: Encontrou a chave '{key}' no chunk {chunk} e alterou seu valor.")
                return
            node = node.next
        node = Node(key, value, self.table[chunk])
        self.table[chunk] = node
        self.size += 1
        # O chunk já continha uma ou mais chaves
        if collision_count > 0:
            self.collision_count += collision_count
            self.__register_log(f"Inserção: Nao encontrou a chave '{key}' no chunk {chunk} e criou a chave. Houve colisao. Total de colisoes: {self.collision_count}")
        # O chunk não continha nenhuma chave previamente
        else:
            self.used_chunk_count += 1 - int(self.used_chunk[chunk])
            self.used_chunk[chunk] = True
            self.__register_log(f"Inserção: Nao encontrou a chave '{key}' no chunk {chunk} e criou a chave.")

    # Deleta uma chave do Hashmap, se a mesma existir
    def delete(self, key):
        chunk = self.__hash(key)
        node = self.table[chunk]
        # O chunk está vazio
        if node == None:
            self.__register_log(f"Remoção: Nao encontrou a chave '{key}' no chunk {chunk}.")
            return
        # O primeiro node do chunk é o que possui a chave procurada
        if node.key == key:
            self.table[chunk] = self.table[chunk].next
            self.used_chunk[chunk] = False
            self.used_chunk_count -= 1
            self.size -= 1
            self.__register_log(f"Remoção: Encontrou a chave '{key}' no chunk {chunk} e a deletou.")
            return
        # Inicia a busca pela chave
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
