import pandas as pd
import streamlit as st
from def_db import conectar_bd
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