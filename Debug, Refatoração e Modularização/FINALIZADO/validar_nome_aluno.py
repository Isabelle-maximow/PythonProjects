def validar_nome_aluno():
    while True:
        nome = input("Digite nome e sobrenome do aluno (mínimo 3 letras): ").strip()
        if len(nome) >= 3 and nome.replace(" ", "").isalpha():
            print("Nome Válido!")
            return nome
        else:
            print("Entrada inválida. Tente novamente.")
