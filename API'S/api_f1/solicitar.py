def solicitar():
    while True:
        try:
            numero_piloto = input("Digite o número do piloto desejado e '0' caso deseje encerrar: ")
            if numero_piloto == "0":
                print("Desligando Sistema...")
                break
        except ValueError:
            print("Digite um número válido!")
        url = f"https://api.openf1.org/v1/drivers?driver_number={numero_piloto}"
        return url