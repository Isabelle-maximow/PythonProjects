# https://economia.awesomeapi.com.br/json/last/USD-BRL&quot

# api publica
# dolar, euri, bitcoin

import requests
# url = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL" # add EUR-BRL,BTC-BRL paea ver o euro e o bitcoin

# response = requests.get(url)
   
# response.raise_for_status()
 
# dados = response.json()

# print (f"Dólar: R${dados["USDBRL"]["bid"]}")
# print (f"Euro: R${dados["EURBRL"]["bid"]}")
# print (f"Bitcon: R${dados["BTCBRL"]["bid"]}")

# CONVERTENDO EM REAIS PARA...
url = "https://economia.awesomeapi.com.br/json/last/BRL-USD,BRL-EUR,BRL-BTC" 

response = requests.get(url)
   
response.raise_for_status()
 
dados = response.json()

print (f"Dólar: R${dados["USDBRL"]["bid"]}")
print (f"Euro: R${dados["EURBRL"]["bid"]}")
print (f"Bitcon: R${dados["BTCBRL"]["bid"]}")
