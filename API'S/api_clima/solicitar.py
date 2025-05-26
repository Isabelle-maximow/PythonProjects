
def solicitar():
    while True:
        try:
            latitude = float(input("Digite a latitude ou '0' para sair: "))
            if latitude == 0:
                print("Saindo...")
                break
            longitude = float(input("Digite a longitude: "))
            url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
            return url
        except ValueError:
            print("Coordenadas inválidas. Tente novamente.")
