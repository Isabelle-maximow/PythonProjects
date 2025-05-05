'''
O try-except é usado para lidar com exceções
em Python, ou seja,
erros que podem ocorrer durante a execução do programa.
Com ele, podemos evitar que o programa seja
interrompido devido a um erro inesperado.
'''


try:
    num = int(input("Digite um número: "))
    resultado = 10 / num
    print(f"Resultado: {resultado}")
except ZeroDivisionError:  # divisão por zero
    print("Erro: Divisão por zero não é permitida.")
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite um número inteiro.")
except Exception as e:
    print(f"Erro inesperado: {e}")

#   usar else como saida
try:
    arquivo = open("Dados.txt", "r") # r=read=leitura
except FileNotFoundError:
    print("Erro ao abrir o arquivo.")
else:
    conteudo = arquivo.read() # isso aqui é o que vai ser lido
    print(f"conteudo do arquivo: {conteudo}")
    arquivo.close() # para fechar o arquivo
    
#   usar finally para fechar o arquivo - sempre é executadocom o sem erro
try:
    numero_x = int(input("Digite um número: "))
    resultado_x = 10 / numero_x
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
else:
    print(f"Resultado: {resultado_x}")
finally:
    print("Execução finalizada com sucesso.")
    
# tratar erro de uma lista, acessando pelo indice invalido:
lista = [1, 2, 3]
try:
    indice = int(input("Digite um índice (0 a 2): "))
    valor = lista[indice]
    print(f"Valor no índice {indice}: {valor}")
except IndexError:
    print ("Erro: Índice fora do intervalo da lista.")
except ValueError:
    print("Erro: Digite um número válido.")
    