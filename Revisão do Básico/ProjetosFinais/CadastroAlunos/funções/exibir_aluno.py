
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