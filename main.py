from classes import API, Structs

# Variaveis de ambiente
RETRIEVE_FROM_API = False
# -----------------------------------------------------------------------------

if RETRIEVE_FROM_API:
    API.get_data()

hm = Structs.hashmap_by_discovery_year()