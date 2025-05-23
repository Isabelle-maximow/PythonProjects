#Aplicação 6
'''
API fórmula 1
Pilotos e seus números:
Max Verstappen: #1
Lando Norris: #4
Gabriel Bortoleto: #5
Isack Hadjar: #6
Jack Doohan: #7
Pierre Gasly: #10
Kimi Antonelli: #12
Charles Leclerc: #16
Oliver Bearman: #87
Liam Lawson: #30
Lewis Hamilton: #44
Oscar Piastri: #81
'''
import requests

def solicitar():
    while True:
        try:
            numero_piloto = input("Digite o número do piloto desejado e '0' caso deseje encerrar: ")
            if numero_piloto == "0":
                print("Desligando Sistema...")
                break
            url = f"https://api.openf1.org/v1/drivers?driver_number={numero_piloto}"
            dados = requisicao(url)
            piloto(dados)
        except ValueError:
            print("Digite um número válido!")

def requisicao(url):
    response = requests.get(url)
    response.raise_for_status()
    dados = response.json()
    return dados

def piloto(dados):
    if len(dados) > 0:
        piloto = dados[0]
        print("Informações do Piloto:")
        print(f"Nome: {piloto.get('full_name', 'Desconhecido')}")
        print(f"Equipe: {piloto.get('team_name', 'Não disponível')}")
        print(f"Nacionalidade: {piloto.get('country_code', 'Não informada')}")
        print(f"Número do carro: {piloto.get('driver_number', 'N/A')}")
        print(f"URL da foto: {piloto.get('headshot_url', 'Sem imagem disponível')}")
    else:
        print("Nenhum dado encontrado para esse piloto.")

if __name__ == "__main__":
    solicitar()