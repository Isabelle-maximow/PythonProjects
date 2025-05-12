
# LISTA
# Listas são estruturas de dados mutáveis, ou seja, podem ser alteradas após a criação.
lista = [1, 2, 3]

# Para se obter o ultimo elemento da lista:
ultimo = lista[-1]
print(ultimo)

# Para acessar uma sequencia da lista - usar o [:] :
sequencia = lista[1:3]
print(sequencia)

# modificar a lista:
lista[0] = 10
print(lista)

# Adicionar um elemento na lista - usar o append : 
lista.append(4)
print(lista)

# Remover um elemento da lista - usar o pop :
remover = lista.pop(0)
print(lista)

# Tamanho da lista - usar o len :
tamanho = len(lista)
print(tamanho)

# ---------------------------------- # ----------------------------------- #
# EXEMPLO DE USO - LISTA
# Cadastrar nome em uma lista:
lista_nomes = []
# deixar smp a lista fora do loop 
while True:
    nome = input('Digite o nome: ')
    lista_nomes.append(nome)
    print(f"Cliente {nome} cadastrado com sucesso!") 
    # input para sair do loop:
    continuar = input('Deseja cadastrar outro cliente? (s/n): ').lower()
    if continuar != 's':
        print('Saindo do Sistema...')
        break

# ---------------------------------- # ----------------------------------- #

# TUPLA
# Tuplas são estruturas de dados imutáveis, ou seja, não podem ser alteradas após a criação.
# Tuplas são definidas com parênteses () e os elementos são separados por vírgulas.
tupla = (1, 2, 3)

# Para acessar um elemento da tupla:
elemento = tupla[0]
print(elemento)

# Para acessar o ultimo elemento da tupla:
ultimo = tupla[-1]
print(ultimo)

# Para acessar uma sequencia da tupla :
sequencia = tupla[1:3]
print(sequencia)

# Tamanho da tupla:
tamanho = len(tupla)
print(tamanho)

# Valor maximo da tupla - usando o max :
maximo = max(tupla)
print(maximo)

# Valor minimo da tupla - usando o min :
minimo = min(tupla)
print(minimo)

# Somar valores da tupla - usando o sum :
soma = sum(tupla)
print(soma)

# Media da tupla - usando o sum e o len :
media = sum(tupla) / len(tupla)
print(media)

# ---------------------------------- # ----------------------------------- #

# DICIONARIO    
# Dicionários são estruturas de dados que armazenam pares de chave-valor.
dicionario = {
    'nome': 'Isabelle',
    'idade': 20,
    'cidade': 'São Paulo'
}

# Para acessar um valor do dicionário:
valor = dicionario['nome']
print(valor)
# OU
print(dicionario('nome'))

# add uma chave e valor no dicionario:
dicionario['Profissão'] = 'Médico'
print(dicionario)

# Para remover um elemento do dicionário - usando o del :
del dicionario['Profissão']
print(dicionario)
# remover um elemento do dicionario - usando o pop :
remover = dicionario.pop('idade')
print(dicionario)

# somente a chaves do dicionario:
chaves = dicionario.keys()
print(chaves)
# somente os valores do dicionario:
valores = dicionario.values()
print(valores)
# saide de ambos:
itens = dicionario.items()  
print(itens)

# adicionar/ atualizar valores do dicionario:
dicionario["idade"] = 21


