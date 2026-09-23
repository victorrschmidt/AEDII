from classes import API, Structs

# Variáveis de ambiente
RETRIEVE_FROM_API = False
# -----------------------------------------------------------------------------

if RETRIEVE_FROM_API:
    API.get_data()

hashmap_bodyname = Structs.hashmap_by_bodyname()
hashmap_bodyname.debug(True)