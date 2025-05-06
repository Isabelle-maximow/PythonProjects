# origem e importar com a função def:
from soma import soma
from sub import subtracao
from multi import multiplicacao
from div import divisao

# ou, podemos colocar td dentro de um unico arquivo e importar:
# from arquivo import soma, subtracao, multiplicacao, divisao

'''  Calculadora simples com Funçao Def	'''
# função soma:
def soma (a, b):
    return a + b
# função subtração:
def subtracao (a, b):
    return a - b    
# função multiplicação:
def multiplicacao (a, b):
    return a * b
# função divisão:
def divisao (a, b):
    if b!= 0:
        return a / b
    else:
        return "Erro: Divisão por zero não é permitida." 
    
# função calculadora:
def calculadora ():
    # inputs:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Escolha a operação (+, -, *, /): ")
    # operação:
    if operacao == "+":
        print(f"Resultado: {soma(num1, num2)}")
    elif operacao == "-":
        print(f"Resultado: {subtracao(num1, num2)}")
    elif operacao == "*":
        print(f"Resultado: {multiplicacao(num1, num2)}")
    elif operacao == "/":
        print(f"Resultado: {divisao(num1, num2)}")
    else:
        print("Operação inválida.")

# rodar a calculadora:
calculadora() # executar a função