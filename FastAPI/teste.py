# cosumindo a api que criamos
# metodo get com request
import requests 

nome = input("Digite o seu nome para a saudação: ")

# url da API:
url = f"http://127.0.0.1:8000/saudacao/{nome}"

# requisição:
response = requests.get(url)
#erro na requisição:
response.raise_for_status()
# converter para json:
dados = response.json()
# pesquisae a API pela chave:
saudacao = dados["mensagem"] # chave do dicionario

# resultado do get na API:
print(f"{saudacao}")