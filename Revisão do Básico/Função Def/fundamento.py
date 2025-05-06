'''
Em Python, a palavra-chave def é usada para definir
uma função.
Uma função é um bloco de código reutilizável que
realiza uma tarefa específica e pode ser chamada
várias vezes ao longo do programa.
As funções podem receber argumentos (entradas) e
podem ou não retornar um valor.
'''

# sintaxe básica da função:
def nome_de_funcao():
    pass # bloco de codigo
    print("função do texto")
    
# executar a funçaõ - fazer chamada da função:
nome_de_funcao() # chamando a função

# função com argumentos e valores:
def funcao_x (argumento, valores):
    # usar smp q tiver argumentos
    # é preciso retornar (return) os argumentos e valores a função
    return argumento, valores

def funcao_y (
    parametro1,
    parametro2,
    parametro3):
    # outras variaveis:
    x = 10
    y = 10
    z = 10
    # definir os valores dos parametros:
    parametro1 = 10
    parametro2 = 20
    parametro3 = 30
    # operação soma:
    resultado = y + z + parametro1 + parametro2 + parametro3
    print(resultado)
funcao_y(10, 10, 10) # chamando a função

# exemplo simples:
def saudação():
    print("Hello word!")
saudação()  # chamando a função

# exemplo com argumentos:
def cumprimento(nome):
    print(f"olá {nome}!")
cumprimento("Gabriel")  # chamando a função

# somar dois numeros:
def soma (a, b):
    #resultado = a + b
    #return resultado    # retonrar o valor do resultado na função
    return a + b  # retornar o valor da soma

# usando a funçao:
print(" soma de dois numeros")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
somar = soma ( num1, num2) # chamando a função - o ato de somar
print(f"A soma de {num1} + {num2} = {somar}") # resultado da soma

# calcular media de 3 numeros:
def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3

# media de aluno
media = calcular_media(7, 8, 9)
print(f"A média é: {media:.2f}")  # formatar o resultado da media

