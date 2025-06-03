import streamlit as st
from def_buscar import buscar_piloto_por_numero
from def_lista_tds import listar_todos_pilotos
from def_salvar_dados import salvar_dados_piloto
from def_listar import listar_pilotos_conhecidos

def menu_principal():
    st.title("ATUALIZAÇÕES SOBRE FÓRMULA 1")
    st.subheader("Principais informações você encontra aqui", divider=True)
    if "tela" not in st.session_state:
        st.session_state.tela = "menu"
    # BOTOES
    col1, col2, col3, col4 = st.columns(4)
    if col1.button("Buscar informações", use_container_width=True):
        st.session_state.tela = "buscar"
    if col2.button("Listar pilotos", use_container_width=True):
        st.session_state.tela = "listar"
    if col3.button("Salvar dados de piloto", use_container_width=True):
        st.session_state.tela = "salvar"
    if col4.button("Pilotos mais conhecidos", use_container_width=True):
        st.session_state.tela = "conhecidos"

    if st.session_state.tela == "buscar":
        buscar_piloto_por_numero()
    elif st.session_state.tela == "listar":
        listar_todos_pilotos()
    elif st.session_state.tela == "salvar":
        salvar_dados_piloto()
    elif st.session_state.tela == "conhecidos":
        listar_pilotos_conhecidos()
        
    st.divider()
    sentiment_mapping = ["1", "4", "3", "4", "5"]
    selected = st.feedback("stars")
    if selected is not None:
        st.markdown(f"Obrigado pelas {sentiment_mapping[selected]} estrelas!")