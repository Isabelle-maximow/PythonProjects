import requests

# Solicita o nome do jogador
nome = input("Digite o nome do jogador para saber mais: ").strip().lower()

# URL base da API
url = "http://127.0.0.1:8000/"

# Faz a requisição à API
response = requests.get(url)
response.raise_for_status()  # Lança erro se falhar

# Converte resposta para dicionário
dados = response.json()

# Procura o jogador pelo nome (ignorando maiúsculas/minúsculas)
encontrado = None
for id_jogador, info in dados.items():
    if info["nome"].lower() == nome:
        encontrado = info
        break

# Exibe o resultado
if encontrado:
    print(f"\nJogador encontrado:")
    print(f"Nome : {encontrado['nome']}")
    print(f"Idade: {encontrado['idade']}")
    print(f"Time: {encontrado['time']}")
else:
    print("\nJogador não encontrado.")
