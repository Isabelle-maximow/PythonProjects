'''
IDENTIFICAÇÃO
    Dev: Isabelle Ferreira
    RA: 242715216
Data: 07/05/2025

'''
# Ver media 
def media (nota1, nota2, nota3):
    return sum([nota1, nota2, nota3]) / 3

# ver status
def status (media):
    if media >= 6.5:
        print("Aprovado.")
    elif media >= 5 and media < 6.5: 
        print("recuperação")
    else:  
        print("reprovado")

