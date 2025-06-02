from def_db import conectar_bd
import streamlit as st
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