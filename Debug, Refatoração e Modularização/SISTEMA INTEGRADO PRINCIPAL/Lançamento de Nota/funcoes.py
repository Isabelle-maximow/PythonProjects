
# MÓDULO: LANÇAR NOTA ALUNO
def validar_nome_aluno():
    while True:
        nome = input("Digite nome e sobrenome do aluno (mínimo 3 letras): ").strip()
        if len(nome) >= 3 and nome.replace(" ", "").isalpha():
            print("Nome Válido!")
            return nome
        else:
            print("Entrada inválida. Tente novamente.")
# ok
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
               

def cadastrar_alunos():
    alunos = []
    while True:
        try:
            nome = validar_nome_aluno()
            notas = validar_notas()
            media = sum(notas) / len(notas)
            status = "Aprovado" if media >= 7 else "Reprovado"
            alunos.append([nome, notas, media, status])
            print("Informações atualizadas com sucesso!")

            continuar = input("Deseja sair? (s para sim e n para não): ").lower()
            if continuar == "s":
                print("Encerrando o sistema cadastrar alunos...")
                return alunos
            elif continuar == "n":
                print("Continuando o cadastro de alunos...")
                continue
            else:
                print("Opção inválida. Continuando o cadastro.")
        
        except ValueError:
            print("Valor inválido! Digite corretamente.")
        except KeyboardInterrupt:
            print("Operação cancelada pelo usuário.")
        except Exception as erro:
            print(f"Erro inesperado: {erro}")
     
def exibir_alunos(alunos):
    for aluno in alunos:
        print(f"""
        Nome: {aluno[0]}
        Notas: {aluno[1]}
        Média: {aluno[2]:.2f}
        Situação: {aluno[3]}""")

