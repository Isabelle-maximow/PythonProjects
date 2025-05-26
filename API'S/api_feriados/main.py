from api import API
from requisicao import requisicao
from loop import loop

if __name__ == "__main__":
    url = API()
    feriados = requisicao(url)
    loop(feriados)