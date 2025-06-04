import requests

url_base = "http://127.0.0.1:8000"

id = int(input("Digite o ID do produto: "))
url = f"{url_base}/itens/{id}"


response = requests.get(url)
response.raise_for_status()
dados = response.json()

if "mensagem" in dados:
    print("Erro", dados["mensagem"])
else:
    print("Produto encontrado:")
    print(f"ID   : {dados['id']}")
    print(f"Nome : {dados['nome']}")
