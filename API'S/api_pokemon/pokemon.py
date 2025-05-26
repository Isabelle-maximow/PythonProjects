def pokemon():
    while True:
        try:
            pokemon = input("Digite o nome do pokemon ou 's' para sair: ").lower()
            if pokemon == 's':
                print("Saindo...")
                break
            else:
                return pokemon
        except ValueError:
            print("Entrada inválida. Tente novamente.")