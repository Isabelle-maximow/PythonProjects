
import requests
def solicitar(): 
    try:
        cep = input('Digite o cep: ')
        url = f'https://viacep.com.br/ws/{cep}/json/'
        return url
    except ValueError:
        print("Insira um cep válido!")