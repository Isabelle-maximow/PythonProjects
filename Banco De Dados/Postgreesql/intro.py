#aula conexão com o banco de dados
#crud com postgress
#biblioteca de manipulação do bando de dados do postgree
#pip install psycopg2 - psycopg2 é a ponte que permite o Python comunicar com o PostgreSQL. 
#database = seu_nome
import psycopg2
#configuração do servidor de banco de dados postgresql
CONFIG_BANCO={
    "host":"10.104.77.36",
    "user": "postgres",
    "password": "Senai@107",
    "database": "isabelle",
    "port": "5432"
}

def conectar_bd():
    conexao=psycopg2.connector.connect(**CONFIG_BANCO)
    cursor=conexao.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS alunos (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nome VARCHAR(100) NOT NULL,
                    nota1 FLOAT NOT NULL,
                    nota2 FLOAT NOT NULL,
                    media FLOAT NOT NULL,
                    situacao VARCHAR(20) NOT NULL)''')
    conexao.commit()
    return conexao,cursor

