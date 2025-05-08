'''
IDENTIFICAÇÃO
    Dev: Isabelle Ferreira
    RA: 242715216
Data: 08/05/2025
'''

from funçoes import converter
from funçoes import resultado

cotacao_dolar = float(input("Digite a cotação do dólar $:"))
quantidade_reais = float(input("Digite a quantidade em reais R$:"))


valor_dolares = converter(cotacao_dolar, quantidade_reais)
resultado()