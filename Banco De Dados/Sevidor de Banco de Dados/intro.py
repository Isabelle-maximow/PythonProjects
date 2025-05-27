#aula20 conectar com o servidor de banco de dados mariadb
#servidor: 
#user:root
#senha:Senai@107
#porta:3306
#database:ISABELLE

# pip install mysql.connector 

import mysql.connector

# configuração do servidor do banco de dados:
CONFIG_BANCO = {
    "host": "10.104.77.36",
    "user": "root",
    "password": "Senai@107",
    "database": "isabelle"
}

# função criar o banco de dados:
def conectar_db():
    conexao = mysql.connector.connect(**CONFIG_BANCO) # conectando com o banco de dados
    cursor = conexao.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS alunos(
                       id INT AUTO_INCREMENT PRIMARY KEY,
                       nome VARCHAR(100) NOT NULL,
                       nota1 FLOAT NOT NULL,
                       nota2 FLOAT NOT NULL,
                       nota3 FLOAT NOT NULL,
                       media FLOAT NOT NULL,
                       situacao VARCHAR(25) NOT NULL )''')
    conexao.commit()
    return conexao, cursor

#conectar_db()

# função para nome:
def validar_nome_aluno():
    while True:
        nome = input("Digite nome e sobrenome do aluno (mínimo 3 letras): ").strip()
        if len(nome) >= 3:
            print("Nome Válido!")
            return nome
        else:
            print("Entrada inválida. Tente novamente.")
        
# função validar notas:
def validar_notas():
    notas = []
    for i in range(1,4):
        while True:
            try:
                nota = float(input(f"Digite a nota {i} (de 0 a 10): "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    print("Nota Válida!")
                    break
                else:
                    print("Nota fora do intervalo permitido. Tente novamente.")
            except ValueError:
                print("Valor inválido! Digite um número.")
    return notas

# calculo media:
def calcular_media(notas):
    media = sum(notas) / len(notas)
    situacao = "Aprovado" if media >= 6 else "Reprovado"
    return media, situacao

# cadastrar aluno:
def cadastrar_aluno():
    conexao, cursor = conectar_db()
    nome = validar_nome_aluno()
    notas = validar_notas()
    media, situacao = calcular_media(notas)  
    # cadastrar alunop no mariadb:
    cursor.execute(""" INSERT INTO alunos (
            nome, nota1, nota2, nota3, media, situacao) VALUES (%s, %s, %s, %s, %s, %s)""", # comando SQL para inserir dados %s pq são variáveis
            (nome, notas[0], notas[1], notas[2], media, situacao)) # inserindo os dados na tabela alunos
    
    conexao.commit()
    conexao.close()
    print(f"Aluno {nome} cadastrado com sucesso!")
    
# exibir alunos cadastrados:
def exibir_alunos():
    conexao, cursor = conectar_db()
    cursor.execute("SELECT * FROM alunos") # selecionando todos os alunos cadastrados
    alunos = cursor.fetchall() # obtendo todos os alunos cadastrados (no pyhton)
    conexao.close()
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        print("-"*30)
        print("Alunos cadastrados:")
        for aluno in alunos:
            print(f"""ID: {aluno[0]},
                  Nome: {aluno[1]}, 
                  Nota1: {aluno[2]}, 
                  Nota 2: {aluno[3]}, 
                  Nota 3: {aluno[4]}, 
                  Média: {aluno[5]}, 
                  Situação: {aluno[6]}""")
            print("-"*30)
    
# atualizar alunos:
def atualizar_alunos():
    conexao, cursor = conectar_db()
    exibir_alunos()
    try:
        id_aluno = int(input("Digite o id do aluno para atualizar: "))
        nota1 = float(input("Digite a nova nota 1: "))
        nota2 = float(input("Digite a nova nota 2: "))
        nota3 = float(input("Digite a nova nota 3: "))
        media, situacao = calcular_media(nota1, nota2, nota3)
        cursor.execute("""UPDATE alunos SET 
                    nota1 = %s,
                    nota2 = %s,
                    nota3 = %s,
                    media = %s,
                    situacao = %s
                    WHERE id = %s 
                    """, (nota1[0], nota2[1], nota3[2], media, situacao, id_aluno))
        conexao.commit()
        print("Notas atualizadas com sucesso!")
    except ValueError:
        print("Erro! Digite um id valido.")
    finally:
        conexao.close
        
# deletar aluno:
def deletar_alunos():
    conexao, cursor = conectar_db()
    exibir_alunos()
    try:
        id_aluno = int(input("Digite o id do aluno para atualizar: "))
        cursor.execute("""DELETE FROM alunos WHERE id = %s""", (id_aluno,))
        conexao.commit()
        print("Deletado com sucesso!")
    except ValueError:
        print("Erro! Digite um id valido.")
    finally:
        conexao.close
        
def main():
    while True:
        print(" SISTEMA DE CADASTRO DE ALUNOS")
        print(""" MENU DE OPÇÕES:
              1 - Cadastrar aluno.
              2 - Exibir aluno.
              3 - Atualizar notas.
              4 - Deletar aluno.
              5 - Sair do sistema.""")
        opcao = input("Digite a opção desejada: ")
        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            exibir_alunos()
        elif opcao == "3":
            atualizar_alunos()
        elif opcao == "4":
            deletar_alunos()
        elif opcao == "5":
            print("Saindo do sistema...")
            break
        else:
            print("Opção invalida. Tente novamente...")
            
if __name__ == "__main__":
    main()
    
    
# streamlit
import streamlit as st