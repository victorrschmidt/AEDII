from classes import API, Structs

# Variáveis de ambiente

RETRIEVE_FROM_API = False

# -----------------------------------------------------------------------------

if RETRIEVE_FROM_API:
    API.get_data()

searcher = Structs.searcher()
searcher.run()
