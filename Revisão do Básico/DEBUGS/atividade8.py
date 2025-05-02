# import random
# while True:
#     numero_secreto = random.randint(1,100):
#     tentativa=1
#     palpite = input("Adivinhe o número" 
#     " entre 1 e 100: ")
#     tentativa=+1
#     if palpite = numero_secreto:
#         print("Parabéns! Você acertou!")
#         print("Tentativas: {tentativa}")
#         continue
#     elif palpite < numero_secreto:
#         print("Tente um número maior.")
#     else:
#         print("Tente um número maior.")

# COM OS DEBUGS:
import random
numero_secreto = random.randint(1,100)
tentativa = 0

while True:
    palpite = int(input("Adivinhe o número entre 1 e 100: "))
    tentativa += 1
    if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
        print(f"Tentativas: {tentativa}")
        break
    elif palpite < numero_secreto:
        print("Tente um número maior: ")
    else:
        print("Tente um número menor: ")