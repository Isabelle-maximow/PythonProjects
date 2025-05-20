
def validar_nome_produto():
    while True:
        try:
            nome = input("Nome do produto (mínimo 3 letras): ").strip()
            if len(nome) >= 3:
                return nome
            else:
                print("Nome inválido. (mínimo 3 letras)")
        except Exception as erro:
            print(f"Erro inesperado: {erro}")