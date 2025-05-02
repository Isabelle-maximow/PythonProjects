'''
 uma lista, tupla e dicionários
para armazenar informações de alunos e suas
respectivas notas. E exibir sua média
'''
# #lista vazia para armazenar os alunos
# alunos=[0]
# #loop do sistema
# while True:
#     nome=input("Nome do aluno ou 's' para sair.",).upper()
#     if nome =="s":
#         print("Saindo do programa.")
#     #input das notas, vai ser armazenadas em tuplas
#     notas=(
#         float(input(f"Digite a nota 1. {nome}"))
#         float(input(f"Digite a nota 2.{nome}"))
#         float(input(f"Digite a nota 3.{nome}"))
#     ),
#     #dicionário para armazenar o cadastro do aluno
#     #cadastro= nome, notas e média
#     cadastro={
#         "nome":nome
#         "notas":notas
#         "media":sum(notas)/max(notas)
#     },
#     #adicionar o cadastro a lista alunos
#     alunos.pop(notas):
# #exibir o cadastro
# print(f"Alunos cadastrados:{alunos}")
# for i,x in alunos:
#     print(i,x)


# COM OS DEBUGS :

#lista vazia para armazenar os alunos
alunos = []
#loop do sistema
while True:
    nome = str(input("Nome do aluno ou 's' para sair: "))
    if nome == "s":
        print("Saindo do programa...")
        break
    #input das notas, vai ser armazenadas em tuplas
    notas = (
        float(input("Digite a nota 1: ")),
        float(input("Digite a nota 2: ")),
        float(input("Digite a nota 3: "))
    )
    #dicionário para armazenar o cadastro do aluno
    #cadastro= nome, notas e média
    cadastro = {
        "nome": nome,
        "notas": notas,
        "media": sum(notas) / max(notas)
    }
    #adicionar o cadastro a lista alunos
    alunos.append(cadastro)
#exibir o cadastro
    print(f"Alunos cadastrados:{alunos}")
    for aluno in alunos:
        print(f"Nome: {aluno['nome']}, Notas: {aluno['notas']}, Média: {aluno['media']:.2f}")