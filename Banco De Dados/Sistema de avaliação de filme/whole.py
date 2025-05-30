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
                           SELECT nome, senha FROM users WHERE nome = %s AND senha = %s
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
    senha = st.text_input("Senha: ", type: "password" )
    
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
            
# sistema principal 
def sistema_princiapl():
    st.title("Gerenciador de filmes")
    st.write(f"Usuário logado:{st.session_state["usuario"]}")
    # botão de logout da barra latereal:
    if st.sidebar.button("Sair"):
        st.session_state["logado"] = False # deslogar usuario
        del st.session_state["usuario"] # remover o nome do usuario da sessaõ
        st.rerun()
        
    # abas para organizar as funcionalidades:
    tab1, tab2, tab3, tab4 = st.tabs([
        "Adicionar", "Atualizar", "Deletar", "Visualizar"
    ])
    # aba1: add filmes:
    with tab1:
        st.subheader("Adicionar filmes") 
        nome = st.text_input ("Nome do filme: ")
        ano = st.number_input ("Ano do filme: " min_value = 1900, max_value = 2100, step = 1)
        nota = st.number_input("Nota: ", min_value = 0.0, max_value = 10.0, step = 0.5)
        if st.button("Adicionar"):
            # verificar se os campos estao preenchidos:
            if nome and ano and nota is not None:
                inserir_filme (nome, nota, ano)
            else:
                st.error("Preencha todos os campos!")
                
    # aba2: atualizar notas:
    with tab2:
        st.header("Atualizar notas")
        filmes = ler_filme()
        if filmes:
            # criar uma lista de opções para a selectbox:
            opcoes = [f""" {i[0]}  {i[1]} Nota - {i[2]}""" for i in filmes]
            filme_selecionado = st.selectbox("Selecione o filme: ", opcoes )
            nova_nota = st.number_input("Nota: ", min_value = 0.0, max_value = 10.0, step = 0.5)
            if st.button("Atualizar"):
                # id do filme, obter o index dele 
                id_filme = filmes[opcoes.index(filme_selecionado)][0] # fixa o id 0 para comnparar
                atualizar_filmes(id_filme, nova_nota)
        else:
            st.write("Nenhum filme cadastrado")
            
    # deletar filme
    with tab3:
        st.header("Deletar filme")
        filmes = ler_filme()
        if filmes:
            # criar uma lista de opções para a selectbox:
            opcoes = [f""" {i[0]}  {i[1]} Nota - {i[2]}""" for i in filmes]
            filme_selecionado = st.selectbox("Selecione o filme: ", opcoes )
            if st.button("Deletar"):
                # id do filme, obter o index dele 
                id_filme = filmes[opcoes.index(filme_selecionado)][0] # fixa o id 0 para comnparar
                deletar_filme(id_filme)
        else:
            st.write("Nenhum filme cadastrado")
            
    # exibir filmes
    with tab4:
        st.header("Filmes cadastrados")
        filmes = ler_filme()
        exibir_grafico(filmes)

def main():
    if "logado" not in st.session_state:
        st.session_state ["logado"] = False
    # tela de login ou sistema princiupal:
    if not st.session_state["logado"]:
        tela_login() # mostra a tela de login
    else:
        sistema_princiapl() # sistema princiapl
    
# executar
if __name__ == "__main__":
    main()
        