'''
IDENTIFICAÇÃO
    Dev: Isabelle Ferreira
    RA: 242715216
Data: 07/05/2025
'''
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc <= 18.5:
        print(f"Seu IMC é: {imc:.1f} baixo do peso")
    elif imc <= 24.9:
        print(f"Seu IMC é: {imc:.1f} peso normal")
    else:
        print(f"Seu IMC é: {imc:.1f} sobrepeso")