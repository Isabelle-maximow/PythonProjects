##############################################################
#Aplicação 7

import requests

# URL da API de feriados do Brasil para o ano de 2025
url = "https://brasilapi.com.br/api/feriados/v1/2025"
# Requisição GET
response = requests.get(url)
feriados = response.json()
print("Lista de Feriados Nacionais - 2025:")
print("-" * 40)
# Loop para exibir cada feriado
for feriado in feriados:
    print(f"Nome: {feriado['name']}")
    print(f"Data: {feriado['date']}")
    print(f"Tipo: {feriado['type']}")
    print("-" * 40)
