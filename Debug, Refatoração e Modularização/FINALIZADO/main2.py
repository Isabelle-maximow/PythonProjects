
from cadastrar_alunos import cadastrar_alunos
from exibir_alunos import exibir_alunos

alunos = []
def main():
    print("Sistema de Cadastro de Alunos")
    cadastrar_alunos()
    exibir_alunos(alunos)
    
if __name__ == "__main__":
    main()