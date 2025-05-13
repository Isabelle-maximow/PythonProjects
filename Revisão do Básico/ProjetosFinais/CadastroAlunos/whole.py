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

# terceira função: cadastro de um aluno em lista: nome, notas, media e classificação
def cadastrar_aluno(validar_nome, validar_nota):
    alunos = [] # lista de alunos
    while True:
        nome = validar_nome() 
        notas = validar_nota()
        calculo_media = lambda notas: sum(notas) / len(notas) # calcular a média do aluno com função lambda
        media = calculo_media(notas)
        # verificar a situação do aluno:
        classificacao = "Aprovado" if media >= 6 else "Reprovado"
        # adicionar a lista:
        alunos.append((nome, notas, media, classificacao))
        
        continuar = input("Deseja cadastrar outro aluno? (s/n): ")
        if continuar.lower() != "s":
            print("Cadastros salvos! Encerrado sistemas...")
            break
    return alunos # retornar a lista de alunos cadastrados
# cadastrar_aluno() # teste 

# 4 fução: 
def exibir_alunos(alunos):
    # loop para exibir os alunos cadastrados na vertical:
    print("Lista de Alunos Cadastrados:")
    for aluno in alunos:
        print(f"""
              Nome: {aluno[0]}
              Notas: {aluno[1]}
              Média: {aluno[2]:.2f}
              Classificação: {aluno[3]}""")
    
def main():
    print("Sistema de Cadastro de Alunos")
    alunos = cadastrar_aluno(validar_nome, validar_nota) # chama a função de cadastro
    exibir_alunos(alunos) # chama a função de exibição
    
main() # chama a função principal