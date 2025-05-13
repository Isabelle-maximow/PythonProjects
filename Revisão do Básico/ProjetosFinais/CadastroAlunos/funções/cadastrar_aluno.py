
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