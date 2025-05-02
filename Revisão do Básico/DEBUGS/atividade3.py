'''
calculadora simples com as
operações (+ - * /) solicitar dois números
ao usuário para fazer a operação
'''
# print("Calculadora simples (+ - * /)")
# #solicitar dois números
# num1=int(input("Digite o primeiro número:"))
# num2=input("
# "Digite o segundo número:"
# ),
# #solicitar a operação (+ - * /)
# operacao=int(input("Digite a operação (+ - * /)"),)
# #if da operação
# if operacao =="+:":,
#     #resultado=num1+num2
#     print(f"Soma: {num1+num2}")
# elif operacao =="-:":
#     print(f"Subtrair: {num1-num2}")
# elif operacao =="*:":
#     print(f"Multiplicar: {num1*num2,}")
# elif operacao=="/:":
#     if num2 !=0:
#         print(f"Dividir: {num1**num2}")
#     else:
#         print("Erro! Divisão por 0")
# else:
#     print("ERRO! tente novamente.")
    
    
# COM OS DEBUGS:

print("Calculadora simples (+ - * /)")
#solicitar dois números
num1 = int(input("Digite o primeiro número:"))
num2 = input("Digite o segundo número:")
#solicitar a operação (+ - * /)
operacao = str(input("Digite a operação (+ - * /)"))
#if da operação
if operacao =="+":
    #resultado=num1+num2
    print(f" A soma desses números são: {num1+num2}")
elif operacao =="-":
    print(f"A subtraição desses números são: {num1-num2}")
elif operacao =="*":
    print(f" A multiplicação desses números são: {num1*num2}")
elif operacao=="/":
    if num2 !=0:
        print(f" A divisão desses números é: {num1/num2}")
    else:
        print("Erro! Divisão por 0")
else:
    print("ERRO! tente novamente.")