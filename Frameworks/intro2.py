
'''
Streamlit é uma framework Python poderosa e intuitiva para
criar aplicativos web interativos com foco em visualização de
dados, machine learning e dashboards, sem exigir
conhecimento profundo em desenvolvimento web.

Streamlit funciona com uma abordagem declarativa, onde você
escreve código Python e a interface é gerada automaticamente.

Comandos de Exibição:
st.write(): Exibe texto, números, DataFrames, etc.
st.title(), st.header(), st.subheader(): Define títulos e cabeçalhos.
st.markdown(): Permite usar Markdown para formatação rica.
st.image(), st.audio(), st.video(): Exibe mídia.

Widgets Interativos:
st.button(): Cria um botão.
st.slider(): Cria um controle deslizante.
st.selectbox(), st.multiselect(): Cria menus de seleção.
st.text_input(), st.number_input(): Cria campos de entrada.
'''

import streamlit as st
import pandas as pd # criar tabelas e dataframes
import matplotlib.pyplot as plt # criar gráficos

st.title("Visualização de Dados")
df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 20, 30, 35, 45]
}) # cria o dataframe

st.write("Dados:", df) # exibe o dataframe
st.line_chart(df) # exibe o gráfico de linha
# gráfico com plt:
fig, ax = plt.subplots()  # cria a figura e os eixos do gráfico
ax.plot(df["x"], df["y"])  # plota os dados do DataFrame no gráfico
st.pyplot(fig)  # exibe o gráfico gerado no Streamlit
