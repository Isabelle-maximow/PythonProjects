import requests
import json
import streamlit as st
def salvar_dados_piloto():
    st.subheader("Salve aqui informações importantes sobre o piloto que desejas!")
    numero_piloto = st.text_input("Digite o número do piloto a ser salvo: ")
    if st.button("Buscar e Salvar informações"):
        url = f"https://api.openf1.org/v1/drivers?driver_number={numero_piloto}&session_key=9158"
        try:
            response = requests.get(url)
            response.raise_for_status()
            dados = response.json()
            if dados:
                piloto = dados[0]
                with open(f"piloto_{numero_piloto}.json", "w", encoding="utf-8") as arquivo:
                    json.dump(piloto, arquivo, indent=4, ensure_ascii=False)
                st.markdown(f"Dados salvos no arquivo piloto_{numero_piloto}.json")
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
                print("Nenhum dado encontrado para esse piloto.")
        except requests.exceptions.RequestException as e:
            print(f"Erro ao acessar a API: {e}")