
import requests

def api_url():
    url="https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL,ETH-BRL"
    return url

#requisitando os valores
def requisitando(url):
    response = requests.get(url)
    print(response.status_code)
    dados = response.json()
    return dados, url

def valores(dados):
    #print(dos valores)
    print(f"Dólar R$: {(float(dados["USDBRL"]["bid"])):.2f}")
    print(f"Euro R$: {(float(dados["EURBRL"]["bid"])):.2f}")
    print(f"Bitcoin R$: {(float(dados["BTCBRL"]["bid"])):.2f}")
    print(f"Ethereum R$: {(float(dados["ETHBRL"]["bid"])):.2f}")

def cotacao(dados):
    cotacao_dolar = float(dados["USDBRL"]["bid"])
    cotacao_euro = float(dados["EURBRL"]["bid"])
    cotacao_bitcoin = float(dados["BTCBRL"]["bid"])
    cotacao_etherium = float(dados["ETHBRL"]["bid"])
    quantidade_reais = float(input("Digite a quantidade de Reais R$: "))
    return cotacao_dolar, cotacao_euro, cotacao_bitcoin, cotacao_etherium, quantidade_reais

def loop(cotacao_dolar, cotacao_euro, cotacao_bitcoin, cotacao_etherium, quantidade_reais): 
    while True:
        menu=input("""Menu:
            Escolha a opção desejada de câmbio.
            1-Dólar(USD)
            2-Euro(EUR)
            3-Bitcoin(BTC)
            4-Etherium(ETH)
            0-Sair
            Escolha uma opção: """)

        if menu=="0":
            print("Saindo do sistema......")
            break
        elif menu=="1":
            #conversão
            dolar=quantidade_reais/cotacao_dolar
            #resultado
            print(f"O valor em dólares é: $ {dolar:.2f}")
        elif menu=="2":
            #conversão
            euro=quantidade_reais/cotacao_euro
            #resultado
            print(f"O valor em euro é: ${euro:.2f}")
        elif menu=="3":
            #conversão
            bit_c=quantidade_reais/cotacao_bitcoin
            #resultado
            print(f"O valor em bitcoin é: ${(bit_c)}")
        elif menu=="4":
            #conversão
            etherium=quantidade_reais/cotacao_etherium
            #resultado
            print(f"O valor em etherium é: ${(etherium)}")
        else:
            print("Opção inválida! Tente novamente....")
    return 


if __name__ == "__main__": 
    url = api_url()
    dados, valores = requisitando(url)
    cotacao_dolar, cotacao_euro, cotacao_bitcoin, cotacao_etherium, quantidade_reais = cotacao(dados)
    loop(cotacao_dolar, cotacao_euro, cotacao_bitcoin, cotacao_etherium, quantidade_reais)