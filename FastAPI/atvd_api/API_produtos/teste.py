import requests
BASE_URL = "http://127.0.0.1:8000"

def consumir_todos_produtos():
    resposta = requests.get(f"{BASE_URL}/produtos/")
    if resposta.status_code == 200:
        print("Lista de produtos:", resposta.json())
    else:
        print("Erro ao buscar produtos:", resposta.status_code)

def consumir_produto_por_id(produto_id):
    resposta = requests.get(f"{BASE_URL}/produtos/{produto_id}")
    if resposta.status_code == 200:
        print("Produto encontrado:", resposta.json())
    else:
        print("Erro ao buscar produto:", resposta.status_code)

if __name__ == "__main__":
    consumir_todos_produtos()
    consumir_produto_por_id(1)
    consumir_produto_por_id(99)