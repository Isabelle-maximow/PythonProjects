
from cadastrar_aluno import cadastrar_aluno
from exibir_aluno import exibir_alunos

def main():
    print("Sistema de Cadastro de Alunos")
    alunos = cadastrar_aluno(validar_nome, validar_nota) # chama a função de cadastro
    exibir_alunos(alunos) # chama a função de exibição
    
main() # chama a função principal