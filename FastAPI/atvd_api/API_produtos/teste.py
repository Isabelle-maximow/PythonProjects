import requests
BASE_URL = "http://127.0.0.1:8000"
def buscar_produto_por_id(produto_id):
    resposta = requests.get(f"{BASE_URL}/produtos/{produto_id}")
    if resposta.status_code == 200:
        dados = resposta.json()
        if "mensagem" in dados:
            print("Erro:", dados["mensagem"])
        else:
            print("Produto encontrado:")
            print(f"ID    : {dados['id']}")
            print(f"Nome  : {dados['nome']}")
            print(f"Preço : {dados['preco']}")
    else:
        print("Erro ao buscar produto:", resposta.status_code)

if __name__ == "__main__":
    produto_id = input("Digite o ID do produto que deseja buscar: ")
    if produto_id.isdigit():
        buscar_produto_por_id(int(produto_id))
    else:
        print("Por favor, digite um número inteiro válido para o ID.")