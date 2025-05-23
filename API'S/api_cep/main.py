
from solicitação import solicitar
from resultado import resultado
from requisição import requisiçao

if __name__ == "__main__": 
    url = solicitar()
    dados = requisiçao(url)
    resultado(dados)