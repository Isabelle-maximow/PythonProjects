import pandas as pd
import streamlit as st
from def_db import conectar_bd

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