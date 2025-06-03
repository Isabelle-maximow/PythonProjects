import pandas as pd
import streamlit as st
def listar_pilotos_conhecidos():
    pilotos = [
        {"Nome": "Max Verstappen", "Número": 1},
        {"Nome": "Lando Norris", "Número": 4},
        {"Nome": "Gabriel Bortoleto", "Número": 5},
        {"Nome": "Isack Hadjar", "Número": 6},
        {"Nome": "Jack Doohan", "Número": 7},
        {"Nome": "Oscar Piastri", "Número": 81},
        {"Nome": "Pierre Gasly", "Número": 10},
        {"Nome": "Kimi Antonelli", "Número": 12},
        {"Nome": "Charles Leclerc", "Número": 16},
        {"Nome": "Liam Lawson", "Número": 30},
        {"Nome": "Lewis Hamilton", "Número": 44},
        {"Nome": "Oliver Bearman", "Número": 87}
    ]
    st.subheader("Lista de pilotos mais reconhecidos mundialmente")
    df_pilotos = pd.DataFrame(pilotos)
    st.dataframe(df_pilotos)