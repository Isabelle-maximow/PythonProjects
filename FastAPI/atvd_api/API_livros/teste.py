import requests
BASE_URL = "http://127.0.0.1:8000"

def buscar_livro_por_id(livro_id):
    resposta = requests.get(f"{BASE_URL}/livros/{livro_id}")
    if resposta.status_code == 200:
        dados = resposta.json()
        if "mensagem" in dados:
            print("Erro:", dados["mensagem"])
        else:
            print("Livro encontrado:")
            print(f"ID    : {dados['ID']}")
            print(f"Título: {dados['titulo']}")
            print(f"Ano   : {dados['ano']}")
            print(f"Autor : {dados['autor']}")
    else:
        print("Erro ao buscar livro:", resposta.status_code)

if __name__ == "__main__":
    livro_id = input("Digite o ID do livro que deseja buscar: ")
    if livro_id.isdigit():
        buscar_livro_por_id(int(livro_id))
    else:
        print("Por favor, digite um número inteiro válido para o ID.")