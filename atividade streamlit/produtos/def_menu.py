import pandas as pd
import streamlit as st
from def_db import conectar_bd
from def_cadastrar import cadastrar_produto
from def_exibir import exibir_produtos
from def_atualizar import atualizar_produto
from def_deletar import deletar_produto

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
