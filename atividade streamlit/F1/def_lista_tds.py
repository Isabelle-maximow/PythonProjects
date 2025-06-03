import pandas as pd
import streamlit as st
import requests
def listar_todos_pilotos():
    url = "https://api.openf1.org/v1/drivers?session_key=9158"
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        
        lista_pilotos = []
        for piloto in dados:
            lista_pilotos.append({
                "Nome": piloto.get("full_name", "Desconhecido"),
                "Número": piloto.get("driver_number", "Sem número"),
                "Equipe": piloto.get("team_name", "Equipe desconhecida")
            })
        df = pd.DataFrame(lista_pilotos)
        st.subheader("Lista de pilotos da sessão 9158")
        st.dataframe(df)

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
        st.error(f"Erro ao acessar a API: {e}")