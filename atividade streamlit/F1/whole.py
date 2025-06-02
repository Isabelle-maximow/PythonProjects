import requests
import json
import streamlit as st
import pandas as pd

# Função 1 - Buscar informações do piloto
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

# Função 2 - Mostrar pilotos conhecidos - pretendo usar pandas
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

# Função 3 - Listar todos os pilotos da sessão 9158 - usar pandas tmb
def listar_todos_pilotos():
    url = "https://api.openf1.org/v1/drivers?session_key=9158"
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()

        # Cria lista de dicionários com dados relevantes
        lista_pilotos = []
        for piloto in dados:
            lista_pilotos.append({
                "Nome": piloto.get("full_name", "Desconhecido"),
                "Número": piloto.get("driver_number", "Sem número"),
                "Equipe": piloto.get("team_name", "Equipe desconhecida")
            })

        # Cria DataFrame
        df = pd.DataFrame(lista_pilotos)

        # Exibe no Streamlit (modo app)
        st.subheader("Lista de pilotos da sessão 9158")
        st.dataframe(df)

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
        st.error(f"Erro ao acessar a API: {e}")

# Função 4 - Salvar dados do piloto em um arquivo JSON
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

# Função principal - menu interativo
def menu_principal():
    st.title("ATUALIZAÇÕES SOBRE FÓRMULA 1")
    st.subheader("Principais informações você encontra aqui", divider=True)

    # Inicializa estado da tela
    if "tela" not in st.session_state:
        st.session_state.tela = "menu"

    # Layout de botões
    col1, col2, col3, col4 = st.columns(4)
    if col1.button("Buscar informações", use_container_width=True):
        st.session_state.tela = "buscar"
    if col2.button("Listar pilotos", use_container_width=True):
        st.session_state.tela = "listar"
    if col3.button("Salvar dados de piloto", use_container_width=True):
        st.session_state.tela = "salvar"
    if col4.button("Pilotos mais conhecidos", use_container_width=True):
        st.session_state.tela = "conhecidos"

    # Exibir a tela correspondente
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
        st.markdown(f"Obrigado pelas {sentiment_mapping[selected]} estrelas!.")

# Executar o menu
if __name__ == "__main__":
    menu_principal()

