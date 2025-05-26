
from api_url import api_url
from converte import converte   
from pokemon import pokemon
from main import main
from filtros import filtros

if __name__ == "__main__":
    nome_pokemon = pokemon()  # Chama a função para obter o nome
    if nome_pokemon:  # Se não for 's'
        url, _ = api_url(nome_pokemon)
        dados = converte(url)
        main(dados)
        filtros(dados)