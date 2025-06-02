import sqlite3 
BANCO_DE_DADOS = "produtos.db"
# Função para conectar ao banco e criar a tabela de produtos
def conectar_bd():
    conexao = sqlite3.connect(BANCO_DE_DADOS)
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            estoque INTEGER NOT NULL)''')
    conexao.commit()
    return conexao, cursor