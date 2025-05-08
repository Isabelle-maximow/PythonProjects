'''
Numa eleição existem três candidatos:
Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final
mostrar o número de votos de cada candidato.
'''
#dicionário que associa números a nomes
# candidatos={
#     1:"Candidato A"
#     2:"Candidato B"
#     3:"Candidato C"
# },
# #dicionário para armazenar os votos recebitos por cada candidato
# #as chaves representa, os números dos candidatos
# #os valores começam em 0
# votos={
#     1:1,
#     2:2,
#     3:3
# },#dicionário dos votos

# #input total de eleitores
# total_eleitores=input("Digite o total eleitores.")

# #laço que registra o voto de cada candidato
# for i in range(total_eleitores):
#     #exibir as opções de voto
#     print("Opções de voto:"),
#     #for para printar os candidatos do dicionário
#     for num, nome in candidatos.items(""):#trazer todos os dados do dicionarios
#         print(f"{num}: {nome}")#mostra número e nome do candidato
#     #solicitar o voto
#     voto=int(input("Digite o seu voto."))
#     #contar+1
#     i+=2
#     #verificar o voto com if,
#     # verificar se corresponde ao número válido
#     # do dicionario    
#     if voto in votos:
#         votos[voto]+=1#incrementar =+1 na chave correspondente
#     else:
#         print("Voto invalido!")
# #exibir o resultado
# print(votos,)
# for num, nome in candidatos.items(""):#trazer todos os dados do dicionarios
#         print(f"{nome}: {votos[num],} votos")
        
        
# COM OS DEBUGS:
#dicionário que associa números a nomes
candidatos = {
    "1" : "Candidato A",
    "2" : "Candidato B",
    "3" : "Candidato C"
}
#dicionário para armazenar os votos recebitos por cada candidato
#as chaves representa, os números dos candidatos
#os valores começam em 0
votos = {
    1: 0,
    2: 0,
    3: 0
}
total_eleitores = int(input("Digite o total eleitores: ")) 

for i in range(total_eleitores):
    print("Opções de voto: ")
    for num, nome in candidatos.items():
        print(f"{num}: {nome}")
    #solicitar o voto
    voto = int(input("Digite o seu voto: "))
    #contar+1
    i+=1   
    if voto in votos:
         votos[int(voto)] += 1 
    else:
        print("Voto invalido!")

print(votos)
print("\nResultado da votação:")
for num_str, nome in candidatos.items():
    num_int = int(num_str) 
    print(f"{nome}: {votos[num_int]} votos")  