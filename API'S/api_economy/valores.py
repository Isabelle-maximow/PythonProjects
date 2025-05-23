
def valores(dados):
    #print(dos valores)
    print(f"Dólar R$: {(float(dados["USDBRL"]["bid"])):.2f}")
    print(f"Euro R$: {(float(dados["EURBRL"]["bid"])):.2f}")
    print(f"Bitcoin R$: {(float(dados["BTCBRL"]["bid"])):.2f}")
    print(f"Ethereum R$: {(float(dados["ETHBRL"]["bid"])):.2f}")