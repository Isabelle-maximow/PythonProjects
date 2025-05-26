
import requests
def converte(url):
    response = requests.get(url)
    response.raise_for_status() 
    dados = response.json()
    return dados