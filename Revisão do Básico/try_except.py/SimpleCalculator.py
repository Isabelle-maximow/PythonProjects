'''
faça uma calculadora simples: soma, subtgração, multiplicação e divisão
use o try e except para tratar os erros
'''

print("Calculadora simples (+ - * /)")
try: 
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    #solicitar a operação (+ - * /)
    operacao = str(input("Digite a operação (+ - * /): "))
    #if da operação
    if operacao == "+":
        print(f" A soma desses números são: {num1+num2}")
    elif operacao == "-":
        print(f"A subtraição desses números são: {num1-num2}")
    elif operacao == "*":
        print(f" A multiplicação desses números são: {num1*num2}")
    elif operacao == "/":
        print(f" A Divisão desses números são: {num1/num2}")    
except ZeroDivisionError:  # divisão por zero
    print("Erro: Divisão por zero não é permitida.")
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite um número inteiro.")