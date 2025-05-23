
import requests
def requisitando(url):
    response = requests.get(url)
    print(response.status_code)
    dados = response.json()
    return dados, url
