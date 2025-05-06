from SimpleCalculator2 import Calculadora

def main (): 
    while True: 
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Escolha a operação (+, -, *, /): ")
        # chama a função para calcular:
        funcao = Calculadora (num1, num2, operacao)
        # exibir resultado:
        print(f"O resultado é {funcao}")
# chamar a funcao responsavel por rodar: 
main()