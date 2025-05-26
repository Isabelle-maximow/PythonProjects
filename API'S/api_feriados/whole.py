
import requests
# URL da API de feriados do Brasil para o ano de 2025
def API():
    url = "https://brasilapi.com.br/api/feriados/v1/2025"
    return url
# Requisição GET
def requisicao(url):
    response = requests.get(url)
    feriados = response.json()
    return feriados

# Loop para exibir cada feriado
def loop(feriados):
    print("Lista de Feriados Nacionais - 2025:")
    print("-" * 40)
    for feriado in feriados:
        print(f"Nome: {feriado['name']}")
        print(f"Data: {feriado['date']}")
        print(f"Tipo: {feriado['type']}")
        print("-" * 40)
        
if __name__ == "__main__":
    url = API()
    feriados = requisicao(url)
    loop(feriados)
