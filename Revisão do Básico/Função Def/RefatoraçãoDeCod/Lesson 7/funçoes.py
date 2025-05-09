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