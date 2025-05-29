# streamlit, mariadb e plotly

import mariadb as mdb
import plotly.express as px 
import streamlit as st
import pandas as pd 

CONFIG_BANCO = {
    "host": "10.104.77.36",
    "user": "root",
    "password": "Senai@107",
    "database": "isabelle"
}

def conectar_db_filmes():
    try:
        conexao = mdb.connector.connect(**CONFIG_BANCO) # conectando com o banco de dados
        cursor = conexao.cursor()
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS filmes(
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        nome VARCHAR(100) NOT NULL,
                        nota FLOAT NOT NULL,
                        ano INT NOT NULL,
            
                            )''')
        conexao.commit()
        return conexao, cursor
    except mdb.Error as erro:
        st.error(f"Erro ao conectar a tabela filmes:{erro}")
        return None, None
    
def conectar_db_admins():
    try:
        conexao = mdb.connector.connect(**CONFIG_BANCO) # conectando com o banco de dados
        cursor = conexao.cursor()
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS users (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        nome VARCHAR(100) NOT NULL,
                        senha VARCHAR(10) NOT NULL )''')
        conexao.commit()
        return conexao, cursor
    except mdb.Error as erro:
        st.error(f"Erro ao conectar a tabela de autentificação de usuarios:{erro}")
        return None, None

# conectar_db_filmes()
# conectar_db_admins()

# validar o login:
def validar_login(nome, senha):
    try:
        conexao, cursor = conectar_db_admins()
        if conexao:
            # consulta no banco de dados:
            cursor.execute('''
                           SELECT nome, senha FROM users WHERE nome = %s, senha = %s
                           ''', (nome, senha))
            usuarios = cursor.fetchone() # traz linha por linha o banco
            # retornar o verdadeiro se oo usuario existir, falso caso contrario:
            return usuarios is not None # so vai retornar se noa estiver vazio
        return False
    except IndexError:
        st.error(f"Erro ao conectar")
        return None, None
    
def inserir_filme(nome, ano, nota):
    conexao, cursor = conectar_db_filmes()
    if conexao:
        cursor.execute('''
                       INSERT INTO filmes (nome, nota, ano) VALUES (
                           %s, %s, %s
                       )
                       ''', (nome, nota, ano))
        conexao.commit()
        conexao.close()
        st.success("Filme cadastrado com sucesso!")    