from classes import API, Structs

# Variáveis de ambiente

RETRIEVE_FROM_API = False
APPLY_HUFFMAN = False

# -----------------------------------------------------------------------------

if RETRIEVE_FROM_API:
    print("Resgatando dados da API...")
    API.get_data()
    print("Finalizado.")

if APPLY_HUFFMAN:
    print("Aplicando codificação...")
    huffman = Structs.huffman()
    huffman.encode()
    print("Finalizado.")

searcher = Structs.searcher()
searcher.run()
