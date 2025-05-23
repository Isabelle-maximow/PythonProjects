
import requests
def requisicao(url):  
    response = requests.get(url)
    response.raise_for_status()
    dados = response.json()
    return dados