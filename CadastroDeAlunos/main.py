"""
Construir uma aplicação simples cadastro de aluno
com sqlite, python e framawork stremlit.
construção a aplicação web com frontend, backend e banco de dados
"""

import streamlit as st
import sqlite3 
import pandas as pd

# arquivo de banco de dados:
DATABASE = "alunos.db"
# Conexão com o banco de dados e criar tabelas e colunas:
def conectat_bd():
    conexao = sqlite3.connect(DATABASE)
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            nota1 REAL NOT NULL,
            nota2 REAL NOT NULL,
            nota3 REAL NOT NULL,
            media REAL NOT NULL,
            situacao TEXT NOT NULL)''') 
    conexao.commit() # serve para salvar as alterações
    return conexao, cursor 
# autoincremente é usado para incrementar automaticamente o id do aluno

# inserir novo aluno:
def cadastrar_aluno(nome, nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    situacao = "Aprovado" if media >= 7 else "Reprovado"
    conexao, cursor = conectat_bd() # conecta ao banco de dados
    cursor.execute('''
        INSERT INTO alunos (nome, nota1, nota2, nota3, media, situacao)
        VALUES (?, ?, ?, ?, ?, ?)''', (nome, nota1, nota2, nota3, media, situacao)) # serve para inserir os dados
    conexao.commit() 
    conexao.close() # fecha a conexão com o banco de dados
    
# lista de alunos cadastrados:
def lista_alunos():
    conexao, cursor = conectat_bd() # conecta ao banco de dados
    cursor.execute("SELECT * FROM alunos") # seleciona todos os alunos
    alunos = cursor.fetchall() # busca todos os alunos do banco de dados para o python fazer leitura
    conexao.close() 
    return alunos 

# atualizar alunos:
def atualizar_aluno(id_aluno, nome, nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    situacao = "Aprovado" if media >= 7 else "Reprovado"
    conexao, cursor = conectat_bd() # conecta ao banco de dados
    cursor.execute('''
        UPDATE alunos SET nome = ?, nota1 = ?, nota2 = ?, nota3 = ?, media = ?, situacao = ?
        WHERE id = ?''', (nome, nota1, nota2, nota3, media, situacao, id_aluno)) # serve para atualizar os dados 
    conexao.commit() 
    conexao.close() 
    
# deletar aluno:
def deletar_aluno(id_aluno):
    conexao, cursor = conectat_bd() 
    cursor.execute("DELETE FROM alunos WHERE id = ?", (id_aluno,)) # serve para deletar os dados
    alunos = cursor.fetchall()
    conexao.commit() 
    conexao.close()
    return alunos

# streamlit interface:
def main():
    st.title("Sistema de Gerenciamento de Alunos")
    aba = st.sidebar.selectbox("Selecione a opção", [
            "Cadastro de Aluno", "Lista de Alunos",
             "Atualizar Aluno", "Deletar Aluno"])
    
    if aba == "Cadastro de Aluno":
        st.subheader("Cadastrar Aluno")
        nome = st.text_input("Nome do Aluno: ")
        nota1 = st.number_input("Nota 1: ", min_value=0.0, max_value=10.0, step=0.1)
        nota2 = st.number_input("Nota 2: ", min_value=0.0, max_value=10.0, step=0.1)
        nota3 = st.number_input("Nota 3: ", min_value=0.0, max_value=10.0, step=0.1)
        if st.button("Cadastrar"): # criamos um botão para cadastrar o aluno
            if len(nome.strip()) >= 2:  # strip() remove espaços em branco
                cadastrar_aluno(nome, nota1, nota2, nota3)
                st.success("Aluno cadastrado com sucesso!")
            else:
                st.warning("O nome do aluno deve ter pelo menos 2 caracteres.")
    elif aba == "Lista de Alunos":
        st.header("Lista de Alunos")
        alunos = lista_alunos()
        # converter para dataframe (pandas):
        df = pd.DataFrame(alunos, columns = [
            "ID", "Nome", "Nota 1", "Nota 2", "Nota 3", "Média", "Situação"])
        # exibir a tabela no streamlit:
        st.dataframe(df) # dataframe é uma tabela do pandas
        
    elif aba == "Atualizar Aluno": # pelo ID do aluno
        st.subheader("Atualizar Aluno")
        alunos = lista_alunos()
        if alunos: 
            df = pd.DataFrame(alunos, columns = [
                "ID", "Nome", "Nota 1", "Nota 2", "Nota 3", "Média", "Situação"])
            # atualiazar aluno pelo ID:
            aluno_escolhido = st.selectbox("Selecione o Aluno", df["ID"]) 
            nome = st.text_input("Nome do Aluno: ")
            nota1 = st.number_input("Nota 1: ", min_value=0.0, max_value=10.0, step=0.1)
            nota2 = st.number_input("Nota 2: ", min_value=0.0, max_value=10.0, step=0.1)
            nota3 = st.number_input("Nota 3: ", min_value=0.0, max_value=10.0, step=0.1)
            if st.button("Atualizar"):
                if len(nome.strip()) >= 2:
                    atualizar_aluno(aluno_escolhido, nome.strip(), nota1, nota2, nota3)
                    st.success("Aluno atualizado com sucesso!")
                else:
                    st.warning("O nome do aluno deve ter pelo menos 2 caracteres.")
        else:
            st.info("Nenhum aluno cadastrado para atualizar.")
            
    elif aba == "Deletar Aluno":
        st.subheader("Deletar Aluno")
        alunos = lista_alunos()
        if alunos: 
            df = pd.DataFrame(alunos, columns = [
                "ID", "Nome", "Nota 1", "Nota 2", "Nota 3", "Média", "Situação"])
            # deletar aluno pelo ID:
            aluno_escolhido = st.selectbox("Selecione o Aluno", df["ID"])
            if st.button("Deletar"):
                deletar_aluno(aluno_escolhido)
                st.success("Aluno deletado com sucesso!")
    
        else:
            st.info("Nenhum aluno cadastrado para deletar.")
    
    else:
        st.warning("Selecione uma opção do menu lateral.")

if __name__ == "__main__":
    main() 