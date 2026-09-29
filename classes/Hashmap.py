from typing import Self

# Classe que contém as informações de um corpo celeste
class Body:
    def __init__(self, value: dict):
        self.id = value["id"]
        self.name = value["englishName"] if value["englishName"] else None
        self.is_planet = value["isPlanet"]
        self.mass = value["mass"]["massValue"] * (10 ** value["mass"]["massExponent"]) if value["mass"] else None
        self.volume = value["vol"]["volValue"] * (10 ** value["vol"]["volExponent"]) if value["vol"] else None
        self.density = value["density"]
        self.gravity = value["gravity"]
        self.radius = value["meanRadius"]
        self.average_temperature = value["avgTemp"]
        self.type = {
            "Star": "Estrela",
            "Planet": "Planeta",
            "Dwarf Planet": "Planeta Anão",
            "Asteroid": "Asteroide",
            "Comet": "Cometa",
            "Moon": "Lua"
        }[value["bodyType"]]

    # Mostra as informações do corpo celeste
    def debug(self) -> None:
        print(f"ID: {self.id}")
        print(f"Nome: {self.name if self.name is not None else 'não especificado'}")
        print(f"É um planeta: {'sim' if self.is_planet else 'não'}")
        print(f"Massa: {str(self.mass) + ' kg' if self.mass is not None else 'desconhecida'}")
        print(f"Volume: {str(self.volume) + ' km³' if self.volume is not None else 'desconhecido'}")
        print(f"Densidade: {self.density} g/cm³")
        print(f"Gravidade: {self.gravity} m/s²")
        print(f"Raio médio: {self.radius} km")
        print(f"Temperatura média: {self.average_temperature} kelvin")
        print(f"Tipo de corpo: {self.type}")

# Classe que contém uma chave e os campos para serem armazenados no Hashmap
class Node:
    def __init__(self, key: str, value: dict, next: Self):
        self.key = key
        self.body = Body(value) if value else None
        self.next = next

# Classe Hashmap
class Hashmap:
    def __init__(self, expected_key_amount: int):
        self.log = []
        self.LOAD_FACTOR = 0.75
        self.CAPACITY_FACTOR = 1.13
        self.capacity = int(expected_key_amount * self.CAPACITY_FACTOR) + 1
        self.table = [None] * self.capacity
        self.used_chunk = [False] * self.capacity
        self.used_chunk_count = 0
        self.size = 0
        self.collision_count = 0

    # Mostra as informações do Hashmap
    def debug(self, show_logs: bool=True, show_keys: bool=True) -> None:
        if show_logs:
            print("-------- Logs do Hashmap: --------")
            for log in self.log:
                print(log)
            print("-------- Fim dos Logs do Hashmap --------")
        if show_keys:
            print("-------- Chaves do Hashmap: --------")
            for node in self.table:
                while node is not None:
                    print(f"Chave: '{node.key}'")
                    print(f"Corpo: {node.body.__dict__}")
                    node = node.next
            print("-------- Fim das Chaves do Hashmap --------")
        print("-------- Informações do Hashmap --------")
        print(f"Total de chaves armazenadas: {self.size}")
        print(f"Total de chunks na tabela: {self.capacity}")
        print(f"Total de chunks utilizados: {self.used_chunk_count}")
        print(f"Total de colisões: {self.collision_count}")
        print("-------- Fim do debug --------")

    # Registra uma operação efetuada no Hashmap
    def __register_log(self, text: str) -> None:
        log = f"Log {len(self.log) + 1}: {text}"
        self.log.append(log)

    # Retorna o número hash para uma chave
    def __hash(self, key: str) -> int:
        return hash(key) % self.capacity

    # Insere um node para a nova tabela hash
    def __insert(self, new_table: list[Node], old_node: Node) -> None:
        chunk = self.__hash(old_node.key)
        node = new_table[chunk]
        collision_count = 0
        while node is not None:
            if node.key == old_node.key:
                node.body = old_node.body
                self.collision_count += collision_count
                self.__register_log(f"Inserção: Encontrou a chave '{old_node.key}' no chunk {chunk} e alterou seu valor.")
                return
            collision_count += 1
            node = node.next
        node = Node(old_node.key, None, new_table[chunk])
        node.body = old_node.body
        new_table[chunk] = node
        # O chunk já continha uma ou mais chaves
        if collision_count > 0:
            self.collision_count += collision_count
            self.__register_log(f"Inserção: Não encontrou a chave '{old_node.key}' no chunk {chunk} e criou a chave. Houve colisão. Total de colisões: {self.collision_count}")
        # O chunk não continha nenhuma chave previamente
        else:
            self.used_chunk_count += 1 - int(self.used_chunk[chunk])
            self.used_chunk[chunk] = True
            self.__register_log(f"Inserção: Não encontrou a chave '{old_node.key}' no chunk {chunk} e criou a chave.")

    # Redistribui as chaves para uma tabela maior
    def __rehash(self) -> None:
        self.capacity *= 2
        self.used_chunk = [False] * self.capacity
        self.used_chunk_count = 0
        new_table = [None] * self.capacity
        for old_node in self.table:
            while old_node is not None:
                self.__insert(new_table, old_node)
                old_node = old_node.next
        self.table = new_table
        self.__register_log(f"Aplicou rehashing na tabela. Nova capacidade: {self.capacity}")

    # Retorna o corpo celeste contido em uma chave do Hashmap (ou None, se a chave não existir)
    def get(self, key: str) -> Body:
        chunk = self.__hash(key)
        node = self.table[chunk]
        while node is not None:
            if node.key == key:
                self.__register_log(f"Busca: Encontrou a chave '{key}' no chunk {chunk} e retornou o valor.")
                return node.body
            node = node.next
        self.__register_log(f"Busca: Não encontrou a chave '{key}' no chunk {chunk}.")
        return None

    # Insere uma chave no Hashmap (ou altera seu valor, se a chave já existir)
    def insert(self, key: str, value: dict) -> None:
        chunk = self.__hash(key)
        node = self.table[chunk]
        collision_count = 0
        while node is not None:
            if node.key == key:
                node.body = Body(value)
                self.collision_count += collision_count
                self.__register_log(f"Inserção: Encontrou a chave '{key}' no chunk {chunk} e alterou seu valor.")
                return
            collision_count += 1
            node = node.next
        node = Node(key, value, self.table[chunk])
        self.table[chunk] = node
        self.size += 1
        # O chunk já continha uma ou mais chaves
        if collision_count > 0:
            self.collision_count += collision_count
            self.__register_log(f"Inserção: Não encontrou a chave '{key}' no chunk {chunk} e criou a chave. Houve colisão. Total de colisões: {self.collision_count}")
        # O chunk não continha nenhuma chave previamente
        else:
            self.used_chunk_count += 1 - int(self.used_chunk[chunk])
            self.used_chunk[chunk] = True
            self.__register_log(f"Inserção: Não encontrou a chave '{key}' no chunk {chunk} e criou a chave.")
        # Verifica se é necessário fazer um rehashing
        if self.size / self.capacity > self.LOAD_FACTOR:
            self.__rehash()

    # Deleta uma chave do Hashmap, se a mesma existir
    def delete(self, key: str) -> None:
        chunk = self.__hash(key)
        node = self.table[chunk]
        # O chunk está vazio
        if node is None:
            self.__register_log(f"Remoção: Não encontrou a chave '{key}' no chunk {chunk}.")
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
        while node is not None:
            if node.key == key:
                prev.next = node.next
                self.size -= 1
                self.__register_log(f"Remoção: Encontrou a chave '{key}' no chunk {chunk} e a deletou.")
                return
            prev = node
            node = node.next
        self.__register_log(f"Remoção: Não encontrou a chave '{key}' no chunk {chunk}.")
