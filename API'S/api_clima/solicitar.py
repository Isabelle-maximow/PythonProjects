
def solicitar():
    latitude = float(input("Digite a latitude: "))
    longitude = float(input("Digite a longitude: "))
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    return url
