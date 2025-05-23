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
    while True:
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
        
        # input para mais cadastros:
        continuar = input("Digite 's' para sair ou qualquer tecla para continuar... ").lower()
        if continuar == "s":
            print("saindo do sistema...")
            break

conectar_db()