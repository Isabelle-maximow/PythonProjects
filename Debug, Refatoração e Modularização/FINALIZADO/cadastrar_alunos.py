from validar_nome_aluno import validar_nome_aluno
from validar_notas import validar_notas

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