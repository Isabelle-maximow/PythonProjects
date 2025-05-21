# https://pokeapi.co/api/v2/pokemon/

# poke-api

import requests

# nome do pokemon para a busca:
pokemon = input('Digite o nome do pokemon: ')
url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}/'

# metodo get na api:
response = requests.get(url)

# erro na requisição:
response.raise_for_status() 
# converter para json:
dados = response.json()

# pesdquisar na api: nome peso e altura:
nome = dados["name"]
alt = dados["height"]
peso = dados["weight"]


print(f'pokemon: {nome.title()}') # .title () primeira letra maiuscula
print(f'Peso: {peso} kg')
print(f'Altura: {alt/10} cm')


# separando em funções 
import requests

# nome do pokemon para a busca:
pokemon = input('Digite o nome do pokemon: ')

def api_url():
    # url da api:
    url = "https://pokeapi.co/api/v2/pokemon/"
    return url

def converte(url):
    # metodo get na api:
    response = requests.get(url)

    # erro na requisição:
    response.raise_for_status() 
    # converter para json:
    dados = response.json()
    return dados

def main(dados):
    nome = dados["name"]
    alt = dados["height"]
    peso = dados["weight"]


print(f'pokemon: {nome.title()}') # .title () primeira letra maiuscula
print(f'Peso: {peso} kg')
print(f'Altura: {alt/10} cm')

# filtro para habilidades:
for habilidade in dados["abilities"]:
    print(f'Habilidades: {habilidade["ability"]["name"]}')

# filtro para habilidades:
for habilidade in dados["abilities"]:
    print(f'Habilidades: {habilidade["ability"]["name"]}')

