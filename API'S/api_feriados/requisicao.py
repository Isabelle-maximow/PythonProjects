
import requests
def requisicao(url):
    response = requests.get(url)
    feriados = response.json()
    return feriados