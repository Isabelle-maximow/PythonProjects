'''
IDENTIFICAÇÃO
    Dev: Isabelle Ferreira
    RA: 242715216
Data: 08/05/2025
'''

def correto(resposta, numero, i, total_acertos, total_erros):
    if resposta == numero * i:
        print("Você acertou!")
        total_acertos += 1
    else:
        print(f"Você errou! O correto é {numero * i}")
        total_erros += 1
    return total_acertos, total_erros

def total(total_acertos, total_erros):
    print(f"Total de acertos: {total_acertos} | Total de erros: {total_erros}")