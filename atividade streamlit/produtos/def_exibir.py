import pandas as pd
import streamlit as st
from def_db import conectar_bd
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