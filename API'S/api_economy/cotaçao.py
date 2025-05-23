
def cotacao(dados):
    cotacao_dolar = float(dados["USDBRL"]["bid"])
    cotacao_euro = float(dados["EURBRL"]["bid"])
    cotacao_bitcoin = float(dados["BTCBRL"]["bid"])
    cotacao_etherium = float(dados["ETHBRL"]["bid"])
    quantidade_reais = float(input("Digite a quantidade de Reais R$: "))
    return cotacao_dolar, cotacao_euro, cotacao_bitcoin, cotacao_etherium, quantidade_reais
