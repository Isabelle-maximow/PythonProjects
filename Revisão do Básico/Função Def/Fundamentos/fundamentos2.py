# ex de função com multiplos argumentos

# função que soma um num variavel de argumento - usando *
def somar_n_num (*numeros):
    return sum(numeros)
print(somar_n_num (10,5,2,10,5,4,10))