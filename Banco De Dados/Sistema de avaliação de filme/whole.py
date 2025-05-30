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
        
# ler os filmes do bando de dados:
def ler_filme():
    conexao, cursor = conectar_db_filmes()
    if conexao:
        cursor.execute('''
                       SELECT id, nome, nota FROM filmes
                       ''')
        # obter dados com o fetchall:
        filmes = cursor.fetchall()
        return filmes # retorna a lista de filmes
    return[] # lista vazia se n tiver filmes cadastrados

# atualizar a nota do filme:
def atualizar_filmes(id_filme, nova_nota):
    conexao, cursor = conectar_db_filmes()
    if conexao:
        cursor.execute('''
                       UPDATE filmes SET nota = %s WHERE id = %s ''',
                       (id_filme, nova_nota))
        conexao.commit()
        conexao.close()
        st.success("Nota atualizada com sucesso!")
        
# deletar um filme:
def deletar_filme(id_filme):
     conexao, cursor = conectar_db_filmes()
     if conexao:
        cursor.execute('''
                        DELETE FROM filmes WHERE id = %s
                        ''', (id_filme,))
        conexao.commit()
        conexao.close()
        st.success("Filme deletado com sucesso!")
        
# função com pandas para criar o dataframe do id, nome, nota e ano:
def exibir_tabela(filmes):
    if filmes:
        # converter o que vem do banco de daods me dataframe:
        df = pd.DataFrame(filmes, columns = [
            "ID", "NOME", "ANO", "NOTA"
        ])
        st.dataframe(df)
        return df
    else:
        st.write("Nenhum filme cadastrado ainda.")
        return None
    
# exibir um grafico em colunas coloridas:
def exibir_grafico(filmes):
    df = exibir_tabela(filmes)
    # if para obter as cores caso ja tenha filme scadastrados:
    if df is not None:
        # definir as cores base nas notas
        df ["Cor"] = df ["Nota"].apply(
            lambda nota: "green" if nota >= 8 else "yellow" if nota >= 5 else "red" )
        # criar grafico de barras com o plotly:
        fig = px.bar(df, x = "Nome", y = "Nota", color = "Cor",
                     color_discrate_map = {
                         "green": "green",
                         "yellow": "yellow",
                         "red" : "red"}, 
                        title = "Notas de filmes", range_y = [0,10])
        st.plotly_chart(fig) # exibir o grafico de barras na tela
        
# tella de login:
def tela_login():
    st.subheader("Digite suas credenciais")
    
    nome_usuarios = st.text_input("Nome do usuário: ")
    senha = st.text_input("Senha: ", type: "password")
    
    if st.button("Entrar"):
        if validar_login(nome_usuarios,senha):
            #marcar como logado:
            st.session_state["logado"] = True
            st.session_state["usuario"] = nome_usuarios
            st.success(f"Login realizado com sucesso {nome_usuarios}!")
            
            # recarregar:
            st.rerun()
        else:
            st.error("Usuário ou senha incorreto!")
            
    
    