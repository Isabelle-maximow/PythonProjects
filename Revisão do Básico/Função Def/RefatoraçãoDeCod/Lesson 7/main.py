'''
IDENTIFICAÇÃO
    Dev: Isabelle Ferreira
    RA: 242715216
Data: 08/05/2025
'''

from funçoes import  verificar_palpite, verificar2, palpite_usuario
import random

numero_secreto = random.randint(1, 100)
tentativa = 0

print("Adivinhe o número de 1 a 100!")
while True:
    palpite, tentativa = palpite_usuario(tentativa)
    if palpite == numero_secreto:
        verificar_palpite(palpite, numero_secreto)
        break
    else:
      verificar2(palpite, numero_secreto)