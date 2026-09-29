# Trabalho de Algoritmos e Estruturas de Dados II

## Autor
Victor Rodrigues Schmidt.

## Utilização
É necessário possuir o Python 3.11 ou superior.

### Instale o projeto
```cmd
git clone https://github.com/victorrschmidt/AEDII.git
```

### Executar

#### Windows
```cmd
py main.py
```

#### Linux
```cmd
python3 main.py
```

## Resumo
Este repósitorio tem como objetivo armazenar os arquivos do trabalho de
Algoritmos e Estruturas de Dados II. O programa extrai dados de corpos celestes
presentes em uma API, e insere os dados em estruturas de Hashmap e Trie.

## Atributos para modelagem
Os atributos relevantes de cada planeta, que são considerados na hora do
armazenamento são:

- ID
- Nome
- Massa
- Volume
- Densidade
- Gravidade
- Raio
- Temperatura
- Tipo

## Estruturas
As estruturas de Hashmap e Trie possuem operações de inserção, busca e remoção
de elementos. O algoritmo de Huffman é responsável por compactar as informações
da API.

## API

### Sobre
A API utilizada para o trabalho é a _The Solar System OpenData_, que contém
informações sobre corpos celestes.

### Link (acessado em 28/09/2026)
https://api.le-systeme-solaire.net

### Endpoint
O módulo da API resgata todos os corpos celestes presentes na API
(cerca de 550 corpos), através da requisição:

https://api.le-systeme-solaire.net/rest/bodies

### Retorno da API
A API retorna um objeto JSON, que contém um array de todos os corpos celestes
presentes na base de dados. Exemplo de um corpo celeste:

```javascript
{
    "id": "skathi",
    "name": "Skathi",
    "englishName": "Skathi",
    "isPlanet": false,
    "moons": null,
    "semimajorAxis": 15541000,
    "perihelion": 0,
    "aphelion": 0,
    "eccentricity": 0.27,
    "inclination": 148.5,
    "mass": {
        "massValue": 3.5,
        "massExponent": 14
    },
    "vol": null,
    "density": 2.3,
    "gravity": 0.0,
    "escape": 0.0,
    "meanRadius": 3.0,
    "equaRadius": 4.0,
    "polarRadius": 0.0,
    "flattening": 0.0,
    "dimension": "",
    "sideralOrbit": 728.2,
    "sideralRotation": 0.0,
    "aroundPlanet": {
        "planet": "saturne",
        "rel": "https://api.le-systeme-solaire.net/rest/bodies/saturne"
    },
    "discoveredBy": "John J. Kavelaars, Brett J. Gladman",
    "discoveryDate": "23/09/2000",
    "alternativeName": "S/2000 S 8",
    "axialTilt": 0,
    "avgTemp": 0,
    "mainAnomaly": 0.0,
    "argPeriapsis": 0.0,
    "longAscNode": 0.0,
    "bodyType": "Moon",
    "rel": "https://api.le-systeme-solaire.net/rest/bodies/skathi"
}
```
