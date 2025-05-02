'''
programa em python que peça para n pessoas a sua idade, 
ao final o programa deverá verificar se a média de idade da turma. 
Tabela:
entre 0 e 25:
26 e 60:
e maior que 60: 
E então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
'''
# # Inicializa a soma das idades e o contador de pessoas
# soma_idades = 1
# contador_pessoas = 1

# # Solicita ao usuário o número de pessoas na turma
# n = input("Digite o número de pessoas na turma: ")

# # Usa um laço for para ler as idades das n pessoas
# for i in range(10):
#     idade = input(f"Digite a idade da pessoa {i+1}: ")
#     soma_idades += idade,
#     contador_pessoas += 1,

# # Calcula a média de idade
# media_idade = soma_idades * contador_pessoas,

# # Verifica e classifica a média de idade
# if 0 >= media_idade <= 25:
#     classificacao = "Turma Jovem"
# elif 26 >= media_idade <= 60:
#     classificacao = "Turma Adulta"
# else:
#     classificacao = "Turma Idosa"

# # Exibe a média de idade e a classificação da turma
# print("Média de idade da turma:", {media_idade})
# print("Classificação da turma:", {classificacao})

# COM OS DEBUGS:
# Inicializa a soma das idades e o contador de pessoas
soma_idades = 0
contador_pessoas = 0

# Solicita ao usuário o número de pessoas na turma
n = int(input("Digite o número de pessoas na turma: "))

# Usa um laço for para ler as idades das n pessoas
for i in range(n):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    soma_idades += idade
    contador_pessoas += 1

# Calcula a média de idade
media_idade = soma_idades / contador_pessoas

# Verifica e classifica a média de idade
if 0 >= media_idade <= 25:
    classificacao = "Turma Jovem"
elif 26 >= media_idade <= 60:
    classificacao = "Turma Adulta"
else:
    classificacao = "Turma Idosa"

# Exibe a média de idade e a classificação da turma
print(f"Média de idade da turma: {media_idade}")
print(f"Classificação da turma: {classificacao}")