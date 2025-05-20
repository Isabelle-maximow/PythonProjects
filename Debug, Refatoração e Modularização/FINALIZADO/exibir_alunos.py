def exibir_alunos(alunos):
    for aluno in alunos:
        print(f"""
        Nome: {aluno[0]}
        Notas: {aluno[1]}
        Média: {aluno[2]:.2f}
        Situação: {aluno[3]}""")
