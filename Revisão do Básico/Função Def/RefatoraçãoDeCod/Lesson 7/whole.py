'''
IDENTIFICAÇÃO
    Dev: Isabelle Ferreira
    RA: 242715216
Data: 08/05/2025
'''

def palpite_usuario(tentativa):
    palpite = int(input("Digite o seu palpite: "))
    tentativa += 1
    return palpite, tentativa

def verificar_palpite(tentativa, numero_secreto):
        print(f"O número secreto é {numero_secreto}.")
        print(f"Tentativas: {tentativa}")
        print("Encerrando o programa.")

def verificar2(palpite, numero_secreto):
    if palpite < numero_secreto:
        print("O número secreto é maior.")
    else:
        print("O número secreto é menor.")
        
import random
# Gerar um número secreto entre 1 e 100
numero_secreto = random.randint(1, 100)
tentativa = 0

print("Adivinhe o número de 1 a 100!")
# Loop para os palpites
while True:
    palpite, tentativa = palpite_usuario(tentativa)
    # Ver os palpite
    if palpite == numero_secreto:
        verificar_palpite(palpite, numero_secreto)
        break
    else:
      verificar2(palpite, numero_secreto)
