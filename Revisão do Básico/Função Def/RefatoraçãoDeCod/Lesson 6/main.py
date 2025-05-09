'''
IDENTIFICAÇÃO
    Dev: Isabelle Ferreira
    RA: 242715216
Data: 08/05/2025
'''

from funçoes import correto, total

total_acertos = 0
total_erros = 0

numero = int(input("Digite um número para treinar a tabuada: "))

for i in range(1, 11):
    resposta = int(input(f"{numero} x {i}? = "))
    total_acertos, total_erros = correto(resposta, numero, i, total_acertos, total_erros)
total(total_acertos, total_erros)