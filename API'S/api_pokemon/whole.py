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

def pokemon():
    while True:
        try:
            pokemon = input("Digite o nome do pokemon ou 's' para sair: ").lower()
            if pokemon == 's':
                print("Saindo...")
                break
            else:
                return pokemon
        except ValueError:
            print("Entrada inválida. Tente novamente.")

def api_url(pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}/"
    return url, pokemon

def converte(url):
    response = requests.get(url)
    response.raise_for_status() 
    dados = response.json()
    return dados

def main(dados):
    nome = dados["name"]
    alt = dados["height"]
    peso = dados["weight"]
    print(f'pokemon: {nome.title()}') # .title () primeira letra maiuscula
    print(f'Peso: {peso} kg')
    print(f'Altura: {alt/10} cm')

def filtros(dados):
    for habilidade in dados["abilities"]:
        print(f'Habilidades: {habilidade["ability"]["name"]}')

if __name__ == "__main__":
    nome_pokemon = pokemon()  # Chama a função para obter o nome
    if nome_pokemon:  # Se não for 's'
        url, _ = api_url(nome_pokemon)
        dados = converte(url)
        main(dados)
        filtros(dados)
