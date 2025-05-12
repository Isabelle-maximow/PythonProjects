""" Projeto de Cadastro Simples
Cadastrar nome e nota de alunos, fazendo sua média e classificação."""

# primeira função: para validar o nome do aluno (mais que 5 caracteres)
def validar_nome():
    while True:
        nome = input("Digite o nome e o sobrenome do aluno: ")
        if len(nome) >=5:
           return nome
        else:
            print("Nome inválido. O nome deve ter pelo menos 5 caracteres!")
# segunda função: para validar a nota do aluno (entre 0 e 10)
def validar_nota():
    notas = [] # armazenar as notas 
    for i in range (1,4):
        while True: # para validação das 3 notas
            nota = float(input(f"Digite a {i}ª nota do aluno (entre 0 e 10): "))
            if nota == 0 or nota <= 10:
                notas.append(nota)   # colocando no dicionario notas
                break
            
            else:
                print(f"A nota {nota} é inválida. A nota deve estar entre 0 e 10!")
    
    return notas # returnar a lista de notas

# terceira função: cadastro de um aluno em lista: nome, notas, media e classificação
def cadastrar_aluno():
    alunos = [] # lista de alunos
    while True:
        nome = validar_nome() 
        notas = validar_nota()
        media = sum(notas) / len(notas) # calcular a média do aluno
