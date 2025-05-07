'''
IDENTIFICAÇÃO
    Dev: Isabelle Ferreira
    RA: 242715216
Data: 07/05/2025
'''
'''
Escreva um programa em python que solicite a cotação do
dólar e solicite a quantidade em real e
converta o valor da moeda pela quantidade colocada
'''

#solicitar ao usuário a cotação do dólar
cotacao_dolar = float(input("Digite a cotação do dólar $:"))

#solicitar ao usuário a quantidade em reais
quantidade_reais = float(input("Digite a quantidade em reais R$:"))

#converter o valor para dólares
valor_dolares = quantidade_reais / cotacao_dolar

#exibir o valor convertido
print(f"O valor em dólares é: ${valor_dolares:.2f}")

