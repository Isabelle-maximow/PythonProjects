import requests

livro = input("Digite o ID do livro que procura: ")
url = "http://127.0.0.1:8000/"

response = requests.get(url)
response.raise_for_status()  
dados = response.json()

if "mensagem" in dados:
    print("Erro", dados["mensagem"])
else:
    print("Produto encontrado:")
    print(f"ID   : {dados['ID']}")
    print(f"Nome : {dados['titulo']}")
    print(f"Ano : {dados['ano']}")
    print(f"Autor : {dados['autor']}")