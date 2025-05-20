# https://api.open-meteo.com/v1/forecast?latitude=-23.5192&longitude=-46.6506122&current_weather=true&quot

# longitude e latitude é FLOAT!

import requests

# inputs de latitude e longitude:
latitude = float(input("Digite a latitude: "))
longitude = float(input("Digite a longitude: "))

# url da api:
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

# request da api metodo get:    
response = requests.get(url)

# erro na requisição:
response.raise_for_status()

# converter para json:
dados = response.json()

# extrair dados:
temperatura = dados["current_weather"] ["temperature"]
velocidade = dados["current_weather"]["windspeed"]

# exibir valores:
print(f"A temperatura atual é: {temperatura}C°")
print(f"A velocidade do vento atual é: {velocidade}km/h")

