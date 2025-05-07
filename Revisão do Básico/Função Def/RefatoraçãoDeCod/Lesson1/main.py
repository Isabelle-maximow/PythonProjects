from funçoes import calculo_fah
from funçoes import calculo_cel

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
