
def validar_preco():
    while True:
        try:
            preco = float(input("Preço do produto (maior que 0.0 R$): "))
            if preco > 0:
                return preco
            else:
                print("Preço inválido.")  
        except ValueError:
            print("Erro: Preço deve ser um número.")
        except Exception as erro:
            print(f"Erro inesperado: {erro}")