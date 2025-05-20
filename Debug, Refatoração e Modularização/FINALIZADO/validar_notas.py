def validar_notas():
    notas = []
    for i in range(4):
        while True:
            try:
                nota = float(input(f"Digite a nota {i + 1} (de 0 a 10): "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    print("Nota Válida!")
                    break
                else:
                    print("Nota fora do intervalo permitido. Tente novamente.")
            except ValueError:
                print("Valor inválido! Digite um número.")
    return notas