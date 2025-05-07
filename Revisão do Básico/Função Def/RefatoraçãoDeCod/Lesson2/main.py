'''
IDENTIFICAÇÃO
    Dev: Isabelle Ferreira
    RA: 242715216
Data: 07/05/2025
'''

from funçoes import media 
from funçoes import status

print("Programa que verifica a média do aluno.")
print("Digite três notas de 0 a 10.")
nome = input("Nome do aluno: ")

#solicitar as três notas ao usuario.
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

#calcular a média.
media = media(nota1, nota2, nota3)

#exibir a média
print(f"A média do aluno {nome} é {media:.2f}")
status(media)