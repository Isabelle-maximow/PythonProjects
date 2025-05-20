
def validar_codigo_produto():
    while True:
        try:
            cod = input("Código do produto (4 dígitos): ")
            if len(cod) == 4 and cod.isdigit(): # esse is_digit() verifica se o código contém apenas dígitos
                return cod
            else:
                print("Código inválido. Deve ter exatamente 4 dígitos.")
                
        except ValueError:
            print("Erro: Código deve conter apenas dígitos.")
        except Exception as erro:
            print(f"Erro inesperado: {erro}")