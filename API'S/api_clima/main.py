
from extrair_dados import extrair_dados
from solicitar import solicitar
from requisição import requisicao

if __name__ == "__main__":
    # rodar o código:
    latitude, longitude = solicitar()
    dados = requisicao()
    temperatura, velocidade = extrair_dados(dados)
    print(f"A temperatura atual é: {temperatura}C°")
    print(f"A velocidade do vento atual é: {velocidade}km/h")