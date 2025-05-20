# pip install requests

# API via CEP -> "https://viacep.com.br/ws/{cep}/json/"

import requests # requisição http

# solicitar o cep do usuario:
cep = input('Digite o cep: ')

# url da api:
url = f'https://viacep.com.br/ws/{cep}/json/'

# fazer a requisição get na API:
response = requests.get(url)  # faz a requisição GET

response.raise_for_status()  # levanta um erro se a requisição falhar

# converter para json:
dados = response.json()

# resultado da requisição com api, as chaves dos dados:
print(f"Endereço: {dados['logradouro']}")
print(f"Bairro: {dados['bairro']}")
print(f"Cidade: {dados['localidade']}")
print(f"Estado: {dados['estado']}")
print(f"UF: {dados['uf']}")
print(f"Região: {dados['regiao']}")