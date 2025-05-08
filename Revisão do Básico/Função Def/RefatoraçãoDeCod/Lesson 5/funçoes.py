'''
IDENTIFICAÇÃO
    Dev: Isabelle Ferreira
    RA: 242715216
Data: 08/05/2025
'''
# def main ():
#     print("Opções de voto:")
#     print("Candidato A vote: 1")
#     print("Candidato B vote: 2")
#     print("Candidato C vote: 3")
#     eleitores = int(input(" Digite o total de eletores: ")) 
#     main2(eleitores)

# def main2 (total_eleitores):
#     candidato1 = 0
#     candidato2 = 0
#     candidato3 = 0
    
#     eleitores_processados = 0
     
#     while eleitores_processados < total_eleitores:
#         # candidatos()
#         voto = input("Digite o seu voto: ")
#         if voto == 1 :
#             print("Voto REALIZADO!")
#             candidato1 += 1
#         elif voto == 2:
#             print("Voto REALIZADO!")
#             candidato2 += 1
#         elif voto == 3:
#             print("Voto REALIZADO!")
#             candidato3 += 1
#         else:
#             print("Voto inválido!")
#             continue  # continue para não perder o voto
#     eleitores_processados += 1
    
def opçoes ():
    print("Opções de voto:")
    print("Candidato A vote: 1")
    print("Candidato B vote: 2")
    print("Candidato C vote: 3")

def registrar_votos(voto, candidato1, candidato2, candidato3):
    if voto == 1 :
        print("Voto REALIZADO!")
        candidato1 += 1
    elif voto == 2:
        print("Voto REALIZADO!")
        candidato2 += 1
    elif voto == 3:
        print("Voto REALIZADO!")
        candidato3 += 1
    else:
        print("Voto inválido!")
   # retornar valores
        return candidato1, candidato2, candidato3, True 
    return candidato1, candidato2, candidato3, False

def resultado(candidato1, candidato2, candidato3):
    print("Resultado da votação:")
    print("Candidato A:", candidato1)
    print("Candidato B:", candidato2)
    print("Candidato C:", candidato3)
    
# funçao principal
def main():
    candidato1 = 0
    candidato2 = 0
    candidato3 = 0
    eleitores_processados = 0
    eleitores = int(input(" Digite o total de eletores: "))
    
    while eleitores_processados < eleitores:
        opçoes()
        voto = int(input("Digite o seu voto: "))
        candidato1, candidato2, candidato3  = registrar_votos(voto, candidato1, candidato2, candidato3)
        eleitores_processados += 1
        resultado(candidato1, candidato2, candidato3)
main()