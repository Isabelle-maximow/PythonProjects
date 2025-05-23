
def extrair_dados(dados):
    temperatura = dados["current_weather"]["temperature"]
    velocidade = dados["current_weather"]["windspeed"]
    return temperatura, velocidade