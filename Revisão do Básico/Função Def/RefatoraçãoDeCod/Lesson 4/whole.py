'''
IDENTIFICAÇÃO
    Dev: Isabelle Ferreira
    RA: 242715216
Data: 08/05/2025
'''
'''
Escreva um programa em python que solicite a cotação do
dólar e solicite a quantidade em real e
converta o valor da moeda pela quantidade colocada
'''

def converter (cotacao_dolar, quantidade_reais):
     return quantidade_reais / cotacao_dolar
def resultado (valor_dolares):
    return print(f"O valor em dólares é: ${valor_dolares:.2f}")

cotacao_dolar = float(input("Digite a cotação do dólar $:"))
quantidade_reais = float(input("Digite a quantidade em reais R$:"))


valor_dolares = converter(cotacao_dolar, quantidade_reais)
resultado()


