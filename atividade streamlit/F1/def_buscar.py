import requests
import streamlit as st
def buscar_piloto_por_numero():
    st.subheader("Buscar informações de um piloto por número")
    numero_piloto = st.text_input("Digite o número do piloto desejado:")

    if st.button("Buscar piloto"):
        if numero_piloto:
            url = f"https://api.openf1.org/v1/drivers?driver_number={numero_piloto}&session_key=9158"
            try:
                response = requests.get(url)
                response.raise_for_status()
                dados = response.json()
                if dados:
                    piloto = dados[0]
                    st.markdown("Informações do Piloto:")
                    st.write(f"**Nome:** {piloto.get('full_name', 'Desconhecido')}")
                    st.write(f"**Equipe:** {piloto.get('team_name', 'Não disponível')}")
                    st.write(f"**Nacionalidade:** {piloto.get('country_code', 'Não informada')}")
                    st.write(f"**Número do carro:** {piloto.get('driver_number', 'N/A')}")
                    foto_url = piloto.get("headshot_url")
                    if foto_url:
                        st.image(foto_url, caption="Foto do piloto", width=200)
                    else:
                        st.info("Sem imagem disponível para este piloto.")
                else:
                    st.warning("Piloto não encontrado para essa sessão.")
            except requests.exceptions.RequestException as e:
                st.error(f"Erro ao acessar a API: {e}")
        else:
            st.warning("Por favor, insira um número de piloto.")