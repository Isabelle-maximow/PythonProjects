'''
Elaborar um programa em Python
que cadastre os dados pessoais como;
(Nome, Sobrenome, Idade, Altura, Peso,)
e calcule o IMC dela e imprima a tabela
do imc
#calcular o IMC
imc = peso /(altura**2);
A tabela do IMC é a seguinte:
resultados menores que 16 — magreza grave;
resultados entre 16 e 16,9 — magreza moderada;
resultados entre 17 e 18,5 — magreza leve;
resultados entre 18,6 e 24,9 — peso ideal;
resultados entre 25 e 29,9 — sobrepeso;
resultados acima de 30 — obesidade;
'''
# print("Calculadora de IMC.")
# #inputs nome-sobrenome, idade,altura e peso
# nome=input("Digite o nome e sobrenome: ")
# idade=int(input("Digite sua idade: "))
# #principais altura e peso.
# altura,=int(input("Digite sua altura em metros: ex: 1.75 metros:... "))
# peso=int(input("Digite seu peso em Quilograma Kg. ex: 100Kg... "),)
# #calculo do imc.
# imc=peso/(altura//2),#
# #exibir o resultado.
# print(f"""
#     Dados pessoais.
#     Nome e Sobrenome:{nome,}
#     Idade: {idade,}
#     Altura: {altura,}
#     Peso: {peso,}
#     IMC: {imc:.2f,}
# """,)
# #if de verificação do imc
# if imc <=16:
#     print("magreza grave.")
# elif 16 >= imc <=16.9:
#     print("magreza moderada")
# elif imc ==17 or imc <= 18.5:
#     print("magreza leve")
# elif imc ==18.6: and imc <=24.9:
#     print("peso ideal;")
# elif imc ==25 and imc <=29,9:
#     print("sobrepeso")
# else:
#     print("Obsidade")

# COM OS DEBUGS
print("Calculadora de IMC.")
#inputs nome-sobrenome, idade,altura e peso
nome = str(input("Digite o nome e sobrenome: "))
idade = int(input("Digite sua idade: "))
#principais altura e peso.
altura = float(input("Digite sua altura em metros: ex: 1.75 metros:... "))
peso = float(input("Digite seu peso em Quilograma Kg. ex: 100Kg... "),)
#calculo do imc.
imc = peso/(altura**2)
#exibir o resultado.
print(f"""
    Dados pessoais.
    Nome e Sobrenome:{nome}
    Idade: {idade}
    Altura: {altura}
    Peso: {peso}
    IMC: {imc:.2f}
""")
#if de verificação do imc
if imc < 16:
    print("magreza grave.")
elif 16 <= imc <= 16.9:    
    print("magreza moderada")
elif 17 <= imc <= 18.5:
    print("magreza leve")
elif 18.6 <= imc <= 24.9:
    print("peso ideal;")
elif 25 <= imc <=29.9:
    print("sobrepeso")
else:
    print("Obesidade")