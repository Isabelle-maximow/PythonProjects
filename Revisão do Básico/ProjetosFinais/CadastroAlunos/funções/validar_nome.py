
# primeira função: para validar o nome do aluno (mais que 5 caracteres)
def validar_nome():
    while True:
        nome = input("Digite o nome e o sobrenome do aluno: ")
        if len(nome) >=5:
           return nome
        else:
            print("Nome inválido. O nome deve ter pelo menos 5 caracteres!")