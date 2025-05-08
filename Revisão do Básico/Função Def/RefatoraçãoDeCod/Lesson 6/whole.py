'''
IDENTIFICAÇÃO
    Dev: Isabelle Ferreira
    RA: 242715216
Data: 08/05/2025
'''
total_acertos = 0
total_erros = 0

def correto (resposta, numero, i, total_acertos, total_erros):
    if resposta == numero * i:
        print("Você acertou!")
        total_acertos += 1
        
    elif resposta != numero * i:
        print(f"Você errou! O correto é {numero * i}")   
        total_erros += 1
    return total_acertos, total_erros
        
def total (total_acertos, total_erros):
    return print(f"Total de acertos: {total_acertos} | Total de erros: {total_erros}")

numero = int(input("Digite um número para treinar a tabuada: "))

for i in range (1, 11):
    resposta = int(input(f"{numero} x {i}? = "))
    correto(resposta, numero, i, total_acertos, total_erros)

total(total_acertos, total_erros)

