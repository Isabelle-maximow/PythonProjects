
import requests
def solicitar(): 
    while True:
        try:
            cep = input("Digite o cep ou 's' para sair: ")
            if cep.lower() == 's':
                print("Saindo...")
                break
            elif not cep.isdigit() or len(cep) != 8:
                print("CEP inválido. Deve conter 8 dígitos.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Tente novamente.")
    url = f'https://viacep.com.br/ws/{cep}/json/'
    return url