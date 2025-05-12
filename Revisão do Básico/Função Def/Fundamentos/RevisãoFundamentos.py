# função com argumentos nomeados (**kargs)
# usado mais para dicionarios
def descrever_pessoa(**infos):
    for chave, valor in infos.items():
        print(f'{chave}: {valor}')
        
# chamando a função com diferentes argumentos nomeados 
descrever_pessoa(nome='Lucas', idade=25, cidade='São Paulo')

# Função lambda em python é uma funçao anonima, parecida com a função def mas armazenada em uma variavel, ela é executada uma vez e descartada 
#sintaxe basica do lambda :
variavel = lambda argumentos, expressao: expressao + variavel

# def X lambda:
def soma(x, y):
    return x + y
somar = soma (10,10)
print(somar)

# lambda
soma = lambda x, y: x + y
print(soma(10,10))

# exemplo dobrar um numero com o def
def dobrar(x):
    return x * 2
# com lambda
dobrar = lambda x: x * 2 # funçaõ lambda são limitadas a uma unica expressão
# lambda se usa para realizar tarefas sem muitas linhas 
print(dobrar(10)) # quando logicamento o cod é menos complexo e não precisa criar uma função que ira se repetir 