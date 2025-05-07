'''
IDENTIFICAÇÃO
    Dev: Isabelle Ferreira
    RA: 242715216
Data: 07/05/2025
'''

from funçoes import calcular_imc
from funçoes import classificar_imc

peso = float(input("Digite seu peso em KG: "))
altura = float(input("Digite sua altura em metros: "))

#fazer o imc
imc = calcular_imc(peso, altura)

print(f"Seu IMC é: {imc:.1f}")
classificar_imc(imc)