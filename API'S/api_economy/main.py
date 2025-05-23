
from api_url import api_url
from requisitando import requisitando
from loop import loop
from cotaçao import cotacao

if __name__ == "__main__": 
    url = api_url()
    dados, valores = requisitando(url)
    cotacao_dolar, cotacao_euro, cotacao_bitcoin, cotacao_etherium, quantidade_reais = cotacao(dados)
    loop(cotacao_dolar, cotacao_euro, cotacao_bitcoin, cotacao_etherium, quantidade_reais)