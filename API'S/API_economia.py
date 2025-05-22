# https://economia.awesomeapi.com.br/json/last/USD-BRL&quot

# api publica
# dolar, euri, bitcoin

import requests
url = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL" # add EUR-BRL,BTC-BRL paea ver o euro e o bitcoin

response = requests.get(url)
   
response.raise_for_status()
 
dados = response.json()

print (f"Dólar: R${dados["USDBRL"]["bid"]}")
print (f"Euro: R${dados["EURBRL"]["bid"]}")
print (f"Bitcon: R${dados["BTCBRL"]["bid"]}")

# CONVERTENDO EM REAIS PARA... - é so colocar como float 
url = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL" 

response = requests.get(url)
   
response.raise_for_status()
 
dados = response.json()

print (f"Dólar: R${float(dados["USDBRL"]["bid"])}") 
print (f"Euro: R${float(dados["EURBRL"]["bid"])}")
print (f"Bitcon: R${float(dados["BTCBRL"]["bid"])}")

# separando em funções

import requests
def api_url():
    url="https://api.exchangerate-api.com/v4/latest/USD"
    return url

def converte(cotacao_dolar, quantidade_real):
    valor_dolar = quantidade_real/ cotacao_dolar
    return valor_dolar

def main():
    url = api_url()
    response=requests.get(url)
    response.raise_for_status()
    dados=response.json()
    cotacao_dolar=(dados["rates"]["BRL"])

    print(f"Cotação do dólar do dia: ${cotacao_dolar}")

    quantidade_reais=float(input("Digite a quantidade de Reais R$: "))
    #conversão
    valor_dolar = converte(cotacao_dolar, quantidade_reais)
    #resultado
    print(f"O valor em dólares é: $:{valor_dolar:.2f}")

if __name__ == "__main__":
    main()

#####################################################################