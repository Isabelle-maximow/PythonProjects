
'''
IDENTIFICAÇÃO
    Dev: Isabelle Ferreira
    RA: 242715216
Data: 24/04/2025

'''
    # 1.1 - Introdução - Revisão de Python
print("Olá, Mundo!")

# Tipos de dados no Python:

var1 = 10 # int

var2 = 10.5 # float

var3 = "Olá, Mundo!" # str

var4 = True # bool

var5 = [1, 2, 3] # list

var6 = (1, 2, 3) # tuple

var7 = {1, 2, 3} # set


# verificar o tipo da variavel:
print(type(var1))

# input de dados e interação:
num_a = int(input("Digite um número para somar: "))
num_b = int(input("Digite outro número para somar: "))
# resultado:
soma = int(num_a) + int(num_b)
# usar o f para integrar variaveis na string: 
print(f"A soma do {num_a} e {num_b} é: {soma}")

    # concatenação de strings:
# juntando nome e sobrenome:
nome = "Isabelle"
sobrenome = "Ferreira"
nome_completo = nome + " " + sobrenome
# resultado:
print(f"Meu nome é: {nome_completo}")

    # transformar a string:
# transformar a string em minusculo:
nome_minusculo = nome_completo.lower()

# Transformar a string em maiusculo:
nome_maiusculo = nome_completo.upper()
  
# contagem de caracteres:
contagem = len(nome_completo)
print(f"A contagem de caracteres do nome completo é: {contagem}")

    # indices e fatiamento:
# acessar o primeiro caractere:
primeiro_caractere = nome_completo[0]
print(f"O primeiro caractere do nome completo é: {primeiro_caractere}")

# ou
print(f"O primeiro caractere do nome completo é: {nome_completo[0]}")

# inverter a ordem 
print(f"O nome completo invertido é: {nome_completo[::-1]}") # usar os dois : e -1

# cortar a string:
texto = "Olá, Mundo!"
print(texto.split("m"))


    # Bloco de codigo e identação:
# if, else e elif:
if True:
    print("Isso é verdadeiro") # edenyação é estar dentro do if ou de outra coisa, ou seja, usar o tab
    if True:
        print("Dentro da segunda condição")
else:
    print("Isso é falso")

    # Laço de repetição:
# for:
numeros = [1, 2, 3, 4, 5]
for i in numeros:
    print(i)
    
# range:
for i in range(10):
    print(i)
    
    #Lista 
# somar números de uma lista:
numeros = [1, 2, 3, 4, 5]
somas = 0
for num in numeros:
    soma = somas + num
    # abreviação
    somas += num
    
print(f"A soma dos números da lista é: {somas}")

    # Enumarate:
# obter indice e valor 
tarefas = ["Estudar", "Trabalhar", "Dormir"]
for indice, tarefas in enumerate(tarefas):
    print(f"Tarefa {indice + 1}: {tarefas}")
    
    
    # Dicionario iterando dicionario
# lista, tuplas e dicionario

# lista:
numeros = [1, 2, 3, 4, 5] # usamos os colchetes []

# tuplas:
numeros = (1, 2, 3, 4, 5) # usamos os parenteses ()

# dicionario:
numeros = {"um": 1, "dois": 2, "tres": 3} # usamos as chaves {} e é acompanhado de valor ""

# na lsia os dados são mutaveis, diferente da tupla, onde os dados n são mutaveis
# o dicionario é um json que é o msm usado para API - td API é Json

# imprimir apenas as chaves do dicionario:
print(dicionario.keys())
# imprimir apenas os valores do dicionario:
print(dicionario.values())
# imprimir chave e valor do dicionario:
print(dicionario.items())
 

# iterar um dicionario:
notas = {
    "Isabelle": 10,
    "Lucas": 9, 
    "Ana": 8
}

# for para fazer a impressão da nota com o nome na vertical:
for aluno, nota in notas.items():
    print(f"{aluno} tirou a nota: {nota}")
    

    # WHILE
# While = Enquanto for vdd ele executa
# usar uma var para ser o contador oq vai ser o controle do while
contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1 # contador = contador + 1 - para ir aumentando o valor co contador 

# loop infinito no while:
# while True:
# usado mts vezes para validação do sistemas
while True:
    sistemas = input("Digite 'S' para sair: ").upper() # upper para deixar tudo em maiusculo
    if sistemas == "S":
        print("Saindo do sistema...")
        break # para sair do loop
    else:
        print("Você digitou: ", sistemas)
