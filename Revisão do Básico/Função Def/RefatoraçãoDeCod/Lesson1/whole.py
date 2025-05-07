'''
IDENTIFICAÇÃO
    Dev: Isabelle Ferreira
    RA: 242715216
Data: 07/05/2025

'''
# FUNÇÃO PARA CONVERTER TEMPERATURA EM FAHRENHEIT 
def calculo_fah (fahren):
    #conversão de fahrenheit para celsius:
    celsius = (fahren - 32)* 5/9  
    return celsius
# FUNÇÃO PARA CONVERTER TEMPERATURA EM CELSIUS
def calculo_cel (celsius):
    #conversão de celsius para fahrenheit:
    fahrenheit = (celsius * 9/5) + 32  
    return fahrenheit

print(""" Sistema para transformar fahrenheit em celsius""")
#solicitar o input da temperatura em fahrenheit
fahren = float(input( "Digite a temperatura em fahrenheit: "))
#converter o input em celcius
celsius = calculo_fah (fahren)  
#print do resultado
print(f""" A temperatura em fahrenheit {fahren} em C° é: {celsius}""")


print("transformar celsius para fahrenheit."),
#input em celsius
cel = float(input("Digite a temperatura em celsius: "))
#operação de converção
fah = calculo_cel (cel)
#resultado
print(f"""A temperatura em C°{cel} em fahrenheit é: {fah}""")
