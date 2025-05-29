import mariadb as mdb

CONFIG_BANCO = {
    "host": "10.104.77.36",
    "user": "root",
    "password": "Senai@107",
    "database": "isabelle"
}
   
def conectar_db_admins():
    try:
        conexao = mdb.connect(**CONFIG_BANCO) # conectando com o banco de dados
        cursor = conexao.cursor()
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS users (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        nome VARCHAR(100) NOT NULL,
                        senha VARCHAR(10) NOT NULL )''')
        conexao.commit()
        return conexao, cursor
    except mdb.Error as erro:
        print(f"Erro ao conectar a tabela de autentificação de usuarios:{erro}")
        return None, None
    
def cadastrar_usuarios(nome, senha):
    conexao, cursor = conectar_db_admins()
    if conexao:
        cursor.execute('''
                       INSERT INTO users (nome, senha) VALUES (
                           %s, %s
                       )
                       ''', (nome, senha))
        conexao.commit()
        conexao.close()
        print(f"Usuário: {nome} | senha: {senha} cadastrado com sucesso!")
        
print("Cadastrar usuario e senha: ")
user = input("Digite o nome de usuario: ")
password = input("Digite a senha: ")
cadastrar_usuarios(user, password)