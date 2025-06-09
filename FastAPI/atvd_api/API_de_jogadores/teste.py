import requests
# Solicita o nome do jogador
nome = input("Digite o nome do jogador para saber mais: ").strip().lower()
# URL base da API
url = "http://127.0.0.1:8000/"
# Faz a requisição à API
response = requests.get(url)
response.raise_for_status() 
dados = response.json()

encontrado = None
for id_jogador, info in dados.items():
    if info["nome"].lower() == nome:
        encontrado = info
        break
if encontrado:
    print(f"\nJogador encontrado:")
    print(f"Nome : {encontrado['nome']}")
    print(f"Idade: {encontrado['idade']}")
    print(f"Time: {encontrado['time']}")
else:
    print("\nJogador não encontrado.")
