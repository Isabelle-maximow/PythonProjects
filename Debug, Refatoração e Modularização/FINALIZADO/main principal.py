from main1 import main
from cadastrar_produto import cadastrar_produto
from main2 import main
from cadastrar_alunos import cadastrar_alunos
from exibir_alunos import exibir_alunos
from exibir_produtos import exibir_produtos
from main3 import main

from crud_usuarios import crud_usuarios

def main():
    while True:
        escolha = input("""
                SISTEMA INTEGRADO:
                1 - Cadastro de Alunos
                2 - Cadastro de Produtos
                3 - Gerenciar Usuários (CRUD)
                4 - Sair do sistema
                Escolha uma opção: """)

        if escolha == "1":
            alunos = cadastrar_alunos()
            exibir_alunos(alunos)

        elif escolha == "2":
            produtos = cadastrar_produto()
            exibir_produtos(produtos)

        elif escolha == "3":
            crud_usuarios()

        elif escolha == "4":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")


# Execução principal protegida com try/except
if __name__ == "__main__":
    try:
        main()
        
    except KeyboardInterrupt:
        print("\nSistema interrompido pelo usuário.")
    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")