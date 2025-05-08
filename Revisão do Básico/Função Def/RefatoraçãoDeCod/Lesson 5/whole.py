'''
IDENTIFICAÇÃO
    Dev: Isabelle Ferreira
    RA: 242715216
Data: 08/05/2025
'''
def main ():
    print("Opções de voto:")
    print("Candidato A vote: 1")
    print("Candidato B vote: 2")
    print("Candidato C vote: 3")
    eleitores = int(input(" Digite o total de eletores: ")) 
    main2(eleitores)

def main2 (total_eleitores):
    candidato1 = 0
    candidato2 = 0
    candidato3 = 0
    
    eleitores_processados = 0
     
    while eleitores_processados < total_eleitores:
        # candidatos()
        voto = input("Digite o seu voto: ")
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
            continue  # continue para não perder o voto
    eleitores_processados += 1

main() 
main2()