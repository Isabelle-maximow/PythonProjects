import sqlite3
import streamlit as st
import pandas as pd

# Configura a página do Streamlit
st.set_page_config(page_title="Sistema de Produtos", page_icon="📦")

# Nome do banco de dados
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

# Função Cadastrar produto
def cadastrar_produto():
    st.subheader("Cadastrar Produto")
    nome = st.text_input("Nome do produto")
    preco = st.number_input("Preço", min_value=0.01, format="%.2f")
    estoque = st.number_input("Estoque", min_value=0, step=1)
    if st.button("Salvar"):
        if nome.strip():
            conexao, cursor = conectar_bd()
            cursor.execute("INSERT INTO produtos (nome, preco, estoque) VALUES (?, ?, ?)",
                           (nome, preco, estoque))
            conexao.commit()
            conexao.close()
            st.success("Produto cadastrado com sucesso!")
        else:
            st.error("O nome do produto deve conter ao menos 3 caracteres.")

# Função Exibir todos os produtos
def exibir_produtos():
    st.subheader("Lista de Produtos")
    conexao, cursor = conectar_bd()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    conexao.close()
    if not produtos:
        st.info("Nenhum produto cadastrado.")
    else:
        df_produtos = pd.DataFrame(produtos)
        st.dataframe(df_produtos)

# Função - Atualizar produto
def atualizar_produto():
    st.subheader("Atualizar Produto")
    conexao, cursor = conectar_bd()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    if not produtos:
        st.info("Nenhum produto cadastrado.")
        return

    opcoes = {f"{p[0]} - {p[1]}": p[0] for p in produtos}
    escolha = st.selectbox("Escolha um produto para atualizar", list(opcoes.keys()))

    if escolha:
        id_produto = opcoes[escolha]
        nome = st.text_input("Novo nome")
        preco = st.number_input("Novo preço", min_value=0.01, format="%.2f")
        estoque = st.number_input("Novo estoque", min_value=0, step=1)

        if st.button("Atualizar"):
            if nome.strip():
                cursor.execute("UPDATE produtos SET nome = ?, preco = ?, estoque = ? WHERE id = ?",
                               (nome, preco, estoque, id_produto))
                conexao.commit()
                st.success("Produto atualizado com sucesso!")
            else:
                st.error("Nome inválido.")
    conexao.close()

# Função - Deletar produto
def deletar_produto():
    st.subheader("Deletar Produto")
    conexao, cursor = conectar_bd()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    if not produtos:
        st.info("Nenhum produto cadastrado.")
        return

    opcoes = {f"{p[0]} - {p[1]}": p[0] for p in produtos}
    escolha = st.selectbox("Escolha um produto para deletar", list(opcoes.keys()))

    if escolha:
        id_produto = opcoes[escolha]
        if st.button("Deletar"):
            cursor.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))
            conexao.commit()
            st.success("Produto deletado com sucesso!")
    conexao.close()

# Interface principal
def menu():
    st.title("Sistema de Gerenciamento de Produtos")
    with st.sidebar:
        st.header("Menu")
        pagina = st.radio("Escolha uma opção:", [
            "Cadastrar produto",
            "Exibir todos os produtos",
            "Atualizar produto",
            "Deletar produto"
        ])

    if pagina == "Cadastrar produto":
        cadastrar_produto()
    elif pagina == "Exibir todos os produtos":
        exibir_produtos()
    elif pagina == "Atualizar produto":
        atualizar_produto()
    elif pagina == "Deletar produto":
        deletar_produto()


# Executa o programa
if __name__ == "__main__":
    menu()
