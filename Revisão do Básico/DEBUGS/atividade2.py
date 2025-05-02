'''
solicitar ao usuário a cotação do dólar
e a quantidade em reais para converter
em dólares, para converter o valor de reais
para dolar.
Divide a quantidade em reais pela cotação
e exibir o valor.
'''
# print("Converter reais para dólares:":)
# #solicitar ao usuário a cotação do dólar
# #dólar do dia ?
# cotacao=int(input(
# "Digite a cotação do dólar do dia $: "))
# #solicitar ao usuário a quantidade em reais
# reais=int(input("
# Digite a quantidade em reaus R$: ")):
# #conversão
# valor_dolar=reais*cotacao#câmbio
# #exibir o valor
# print(f
# "O valor em dólares é: ${valor_dolar:.2f}")

#   COM OS DEBUGS:

print("Converter reais para dólares:")
#solicitar ao usuário a cotação do dólar
#dólar do dia ?
cotacao = int(input("Digite a cotação do dólar hoje: "))
#solicitar ao usuário a quantidade em reais
reais = int(input("Digite a quantidade em reais R$: "))
#conversão
valor_dolar = reais / cotacao #câmbio
#exibir o valor
print(f"O valor em dólares é: ${valor_dolar:.2f}")