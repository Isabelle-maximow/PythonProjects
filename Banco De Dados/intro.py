'''
SQLite é uma biblioteca em linguagem C que implementa
uma base de dados SQL embutida.
Programas que usem a biblioteca SQLite podem ter acesso
a banco de dados SQL sem executar um processo;
SGBD (“Sistema Gerenciador de Banco de Dados”). Em python
o sqlite é utilizado para teste, antes de colocar em produção,
usado para ver o desempenho e comportamento do sistema
antes do deploy.
Sqlite é uma biblioteca que já vem ao instalar o python.
'''

import sqlite3
# este é o sql lite para TESTES

# arquivo do banco de dados:
BANCO_DE_DADOS = "alunos.db" # nome do arquivo do banco

# 1° função que cria o db e inicia e cria a tabela alunos, colunas: nome. notas, media e situação
def conectar_db():
    conexao = sqlite3.connect(BANCO_DE_DADOS) #conectando, caso n existir ele cria
    cursor = conexao.cursor() # abrir uma conexao para comandos sql
    cursor.execute(''' CREATE TABLE IF NOT EXISTS alunos
                   (id INTEGER PRIMARY KEY AUTOINCREMENT,  
                   nome TEXT NOT NULL,      
                   nota1 REAL NOT NULL,
                   nota2 REAL NOT NULL,
                   nota3 REAL NOT NULL,
                   media REAL NOT NULL,
                   situacao TEXT NOT NULL)''')
# REAL = float
# tipo texto que n pode ser nulo
# id auto incremento

# salvar e atualizar o bd:
    conexao.commit()
    return conexao, cursor

# 2° função validar nome
def validar_nome():
    while True:
        try:
            nome = input("Digite o nome do aluno: ")
            if len(nome) >= 5:
                return nome
            else: 
                print ("Nome deve ter pelo menos 5 caracteres!")
        except ValueError:
            print("Digite um nome válido")
            
# 3° função notas
def validar_nota():
    notas = []
    for i in range(1, 4):
        while True:
            try:
                nota = float(input(f"Digite a nota {i} entre 0 a 10: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Nota inválida. Deve estar entre 0 e 10!")
            except ValueError:
                print("Por favor, digite um número válido.")
    return notas

# 4° media 
def calculo_media(notas):
    media = sum (notas)/len(notas)
    situacao = "Aprovado" if media >= 6 else "Reprovado"
    return media, situacao

# 5° cadastrar
def cadastro_aluno():
        conexao, cursor = conectar_db # chamar o banco
        nome = validar_nome()
        notas = validar_nota()
        media, situacao = calculo_media(notas)
        
        # inserir os comandos sql ao banco de dados
        cursor.execute('''INSERT INTO alunos
                       (nome, nota1, nota2, nota3, media, situacao) VALUES (?,?,?,?,?,?)''',
                       (nome,notas[0], notas[1],notas[2],media,situacao))
        # atualizar e salvar:
        conexao.commit()
        # fechar a conexao:
        conexao.close()
        print("aluno cadastado com sucesso!")
        
  
# 6° função exibir a tabela alunos
def exibir_alunos():
    # conctar ao banco:
    conexao,cursor = conectar_db
    # comandos sql:
    cursor.execute("SELECT * FROM alunos")
    # função do python chamada fethall, leitura de dados:
    alunos = cursor,fethall() # leitura sql
    conexao.close()
    
    # loop para exibir no terminal ao sair do sistema:
    for i in alunos:
        print(f"""
              ID: {i[0]},
              Nome: {i[1]},
              Nota1: {i[2]},
              Nota2: {i[3]},
              Nota3: {i[4]},
              Média: {i[5]},
              Situação: {i[6]}
              """) 
        print("-"*30)
        
def atualizar_aluno():
    exibir_alunos()
    conexao,cursor = conectar_db()
    while True:
        try:
            # editar aluno pelo id
            id_aluno = int(input("Digite o ID do aluno para atualizar(ou 0 para sair): "))
            if id_aluno == 0:
                print("Opção cancelada....")
                break
            # verificar se o aluno existe:
            cursor.execute("SELECT id FROM alunos WHERE id=?", (id_aluno,)) # stop da query
            # trazer os dados do bd :
            if cursor.fethall():
                # coletar os dados para atualizar novamente:
                nome = validar_nome()
                notas = validar_nota()
                media,situacao = calculo_media(notas)
                # atualizar os dados na tabela:
                cursor.execute("UPDATE alunos SET nome = ?, nota1=?, nota2=?, nota3=?, media=?, situacao=? WHERE id=?",  
                               (nome,notas[0], notas[1],notas[2],media,situacao, id_aluno))
                conexao.commit()
                print("Aluno atualizado com sucesso")
            else:
                print("ID inválido. Tente novamente")
        except ValueError:
            print("erro") 
            
def deletar_aluno():
    exibir_alunos()
    conexao,cursor = conectar_db()
    while True:
        try:
            # editar aluno pelo id
            id_aluno = int(input("Digite o ID do aluno para deletar(ou 0 para sair): "))
            if id_aluno == 0:
                print("Opção cancelada....")
                break
            # trazer os dados do bd :
            if cursor.fethall():
                cursor.execute("DELETE alunos WHERE id=?", (id_aluno,)) # stop da quer
                conexao.commit()
                print("Aluno atualizado com sucesso")
            else:
                print("ID inválido. Tente novamente")
        except ValueError:
            print("erro") 
            
def main():
    try:
        while True:
            opcao = menu()
            if opcao == "1":
                cadastro_aluno(alunos)
            elif opcao == "2":
                exibir_aluno(alunos)
            elif opcao == "3":
                editar_aluno(alunos)
            elif opcao == "4":
                exibir_situacao(alunos, "Aprovado")
            elif opcao == "5":
                exibir_situacao(alunos, "Reprovado")
            elif opcao == "6":
                print("Saindo do sistemas...")
            else:
                print("Opção inválida, escolha uma opção existente.")
    except ValueError:
        print("Selecine uma opção válida!")
            
if __name__ == "__main__":
    main()     