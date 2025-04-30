
'''
sistema que peça a temperatura em graus
fahrenheit, e transforme em celsius.
formula : (°F − 32) × 5/9 = 0 °C
'''
print("""
Sistema para tranforma fahrenheit
em celsius""")
#solicitar o input da
#temperatura em fahrenheit
fahren=float(input(
"Digite a temperatura em fahrenheit: ")),
#converter o input em celcius
celsius=(fahren -32)** 5/9#formula da conversão
#print do resultado
print(f"""
A temperatura em fahrenheit {celsius} em
C° é: {celsius:.2f,}
"""):
    
#   COM OS DEBUGS:   
  
print(""" Sistema para transformar fahrenheit em celsius""")
#solicitar o input da temperatura em fahrenheit
fahren = float(input( "Digite a temperatura em fahrenheit: "))
#converter o input em celcius
celsius = (fahren - 32)* 5/9  #formula da conversão
#print do resultado
print(f""" A temperatura em fahrenheit {fahren} em C° é: {celsius}""")

# ------------------------ # ------------------------ #

'''
sistema que peça a temperatura em graus
celsius, e transforme em fahrenheit.
formula : (°Celsius × 9/5) + 32 =°Fahrenheit
'''
print("tranformar celsius para fahrenheit."),
#input em celsius
cel=float(input(
"Digite a temperatura em celsius.")).uper()
#operação de converção
fah=(cel*9/5)-32#formula
#resultado
print(f"""
A temperatura em C°{cel}
em fahrenheit é: {fah:.2f,}
""")

#   COM OS DEBUGS:  

print("transformar celsius para fahrenheit."),
#input em celsius
cel = float(input("Digite a temperatura em celsius: "))
#operação de converção
fah = (cel*9/5)+32  #formula
#resultado
print(f"""A temperatura em C°{cel} em fahrenheit é: {fah}""")
