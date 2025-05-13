# Programa com a base do python, print, tipo de dados, operações e expressões matemáticas
# manipulaçõa de strings, estruduta condicionais, listas, tuplas e dicionarios
# tratamento de erros (try-exce´t), função def e lambda.

def menu():
    print("Bem-vindo ao sistema de aprendizagem Python!")
    print("Escolha um tema para aprender:")
    print("""
          1 - Introdução a Print
          2 - Tipos de dados e variaveis
          3 - Operações e expressões matemáticas
          4 - Manipulação de strings
          5 - Estruturas condicionais
          6 - laços de repetição
          7 - Listas e tuplas
          8 - Dicionários
          9 - Tratamento de erros (try-except)
          10 - Funções (def e lambda)
          0 - Sair
     """)
    
# princiapl:
def main():
    while True:
        menu() # exibir o menu
        escolha = int(input("Digite o número do tema desejado: "))
        if escolha == 1:    
            print("Otimo! Vamos entender o uso de Print!")
            print("O comando print é utilizado para exibir mensagens na tela.")
            print("Exemplo principal para todo dev em aprendizado: print('Olá, Mundo!')")
            variavel = "Olá, Mundo!"
            print("Chamamos de uma variavel no print") 
            
            # exe,plo 1:
            print(f"chamar a variavel {variavel} entre o texto")
            # exemplo 2:
            print("colocar o texto e chamar a variavel apos ele", variavel)
        
        elif escolha == 2:
            print("Legal! Vamos entender os tipos de dados e variáveis!")
            print("Os tipos de dados mais comuns em Python são:")
            print("""Os tipos de dados mais comuns em Python são:
            1. Inteiros (int): números inteiros, como 1, 2, 3.
            2. Flutuantes (float): números decimais, como 1.5, 2.7.
            3. Strings (str): sequências de caracteres, como 'Olá'.
            4. Booleanos (bool): valores verdadeiros ou falsos, como True ou False.
            """)
            
        elif escolha == 3:
            print("Genial! Vamos entender operações e expressões matemáticas!")
            print("As operações matemáticas básicas em Python são:")
            print("""1. Adição (+)
            2. Subtração (-)
            3. Multiplicação (*)
            4. Divisão (/)
            5. Módulo (%)
            """)
        
        elif escolha == 4:
            print("Cool! Vamos entender a manipulação de strings!")
            print("As strings são sequências de caracteres e podem ser manipuladas de várias maneiras.")
            print("""Algumas operações comuns com strings são:
            1. Concatenar: juntar duas ou mais strings.
            2. Repetir: repetir uma string várias vezes.
            3. Acessar caracteres: acessar um caractere específico em uma string.
            """)
            
            # exemplos de manipulação de strings:
            print("Exemplo de manipulação de strings:")
            string1 = "Olá, Mundo!"
            print("Colocando em Maiuscula: ", string1.upper())
            print("Colocando em Minuscula: ", string1.lower())
            print("Dividir a string: ", string1.split(","))
        
        elif escolha == 5:
            print("Ótimo! Vamos entender estruturas condicionais!")
            print("As estruturas condicionais permitem executar diferentes blocos de código com base em condições.")
            
            # exemplo de estrutura condicional:
            idade = int(input("Digite sua idade: "))
            if idade < 18:
                print("Você é menor de idade.")
            elif idade == 18:
                print("Você tem 18 anos.")
            else:
                print("Você é maior de idade.")
        
        elif escolha == 6:
            print("Legal! Vamos entender laços de repetição!")
            print("Os laços de repetição permitem executar um bloco de código várias vezes.")
            
            # exemplo de laço while:
            while True:
                print("Este é um laço de repetição infinito. Pressione Ctrl+C para sair.")
                parar = input("Digite s para parar e sair do loop: ")
                if parar.lower() == "s":
                    print("Saindo do laço de repetição.")
                    break
                else:
                    print("Continuando o laço de repetição.")
                    continue
            
            # exemplo de laço de repetição for:
            for i in range(5):
                print(f"Contagem: {i}")
            
        elif escolha == 7:
            print("Amazing! Vamos entender listas e tuplas!")
            print("As listas e tuplas são estruturas de dados que permitem armazenar coleções de itens.")
            print("""1. Listas: são mutáveis e podem ser alteradas após a criação.
                     2. Tuplas: são imutáveis e não podem ser alteradas após a criação.""")
            
            # exemplo de lista:
            lista = ["maça", "melancia", "uva", "morango"]
            print("Lista de frutas: ", lista)
            
            # exemplo de tupla:
            tupla1 = ("maça", "melancia", "uva", "morango")
            tupla2 = (1, 2, 3, 4)
            print(f"Tupla Simples: {tupla1} {tupla2}")
            
        elif escolha == 8:
            print("Muito bom! Vamos entender dicionários!")
            print("Os dicionários são estruturas de dados que armazenam pares de chave-valor.")
            print("Exemplo de dicionário:")
            
            # exemplo de dicionário:
            dicionario = {
                "nome": "João",
                "idade": 25,
                "curso": "Desenvolvimento de Sistemas",
            }
            print(f" Dicionario do aluno com chave e valor: {dicionario} \n")
            
        elif escolha == 9:
            print("Inteligente! Vamos entender o tratamento de erros!")
            print("O tratamento de erros permite lidar com exceções e evitar que o programa pare inesperadamente.")
            
            # exemplo de tratamento de erro:
            try:
                numero = int(input("Digite um número para dividir por 10: "))
                resultado = 10 / numero
                print(f"Resultado: {resultado}")
            except ZeroDivisionError:  # erro qaundo o usuario digita 0
                print("Erro: Divisão por zero não é permitida.")
            except ValueError:  # erro quando o usuario digita um valor diferente de inteiro
                print("Erro: Valor inválido. Digite um número inteiro.")
                
        elif escolha == 10:
            print("Funny! Vamos entender funções (def e lambda)!")
            print("As funções permitem agrupar um bloco de código que pode ser chamado várias vezes.")
            
            # exemplo de função def:
            def soma(a, b):
                return a + b
            resultado = soma(5, 10)
            print(f"Resultado da soma com função DEF: {resultado}")
            
            # exemplo de função lambda:
            multiplicacao = lambda x, y: x * y
            resultado_lambda = multiplicacao(5, 10)
            print(f"Resultado da multiplicação com lambda: {resultado_lambda}")      
            
        elif escolha == 0:
            print("Saindo do sistema. Até logo!")
            break      
        
        else:
            print("Opção inválida. Tente novamente.")
# chama a função principal
main()