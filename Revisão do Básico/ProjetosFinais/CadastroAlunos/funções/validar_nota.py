
# segunda função: para validar a nota do aluno (entre 0 e 10)
def validar_nota():
    notas = [] # armazenar as notas 
    for i in range (1,4):
        while True: # para validação das 3 notas
            try:
                nota = float(input(f"Digite a {i}ª nota do aluno: "))
                if nota == 0 or nota <= 10:
                    notas.append(nota)   # colocando no dicionario notas
                    break
                else:
                    print(f"A nota {nota} é inválida. A nota deve estar entre 0 e 10!")
            except ValueError:
                print("Entrada inválida. Digite uma nota válida")
    return notas # returnar a lista de notas