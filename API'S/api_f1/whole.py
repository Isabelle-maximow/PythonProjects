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
numero_piloto=input("Digite o número do piloto desejado: ")
# URL da API OpenF1
url = f"https://api.openf1.org/v1/drivers?driver_number={numero_piloto}&session_key=9158"
# Requisição GET
response = requests.get(url)
# Verificação de status da requisição
response.raise_for_status()
#converter os dados para json
dados = response.json()
# Verifica se retornou algum piloto
if len(dados) > 0:
    # Pega o resultado da lista da api
    piloto = dados[0]
    # Exibe os dados do piloto
    print("Informações do Piloto:")
    print(f"Nome: {piloto.get('full_name', 'Desconhecido')}")
    print(f"Equipe: {piloto.get('team_name', 'Não disponível')}")
    print(f"Nacionalidade: {piloto.get('country_code', 'Não informada')}")
    print(f"Número do carro: {piloto.get('driver_number', 'N/A')}")
    print(f"URL da foto: {piloto.get('headshot_url', 'Sem imagem disponível')}")
else:
    print("Nenhum dado encontrado para esse piloto na sessão informada.")