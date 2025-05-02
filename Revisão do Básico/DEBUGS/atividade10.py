'''
execicío:
sistema que irá armazenar nome, e-mail e telefone
irá armazenar em três listas nome, email e telefone
deve exibir o dicionário armazenado
'''

# lista_nome=[]
# lista_telefone=[]
# #adicionar tudo em um dicionário
# dicionario_sistema={
#     "nomes":lista_nome
#     "telefone":lista_telefone
#     "email":"lista_email"
# }
# while True:
#     #input nome,telefone,email
#     nome_x=input("Digite o nome:")
#     lista_nome.pop(nome_x)
#     telefone=input("Digite o telefone: ")
#     lista_telefone.pop(telefone)
#     email=input("Digite o e-mail: ")
#     lista_email.pop(email)
#     print(f
# """ Nome: {nome_x,}
#     Telefone: {telefone,}
#     E-mail: {email,}
#     Cadastrados com sucesso!"""```)
#     continuar_x=input("digite "s" para sair ou qualquer tecla para continuar.").lower()
#     if continuar_x.lower=="s":
#         print("Saindo do sistema...)"
#         print(dicionariosistema)#horizontal
# #exibir dicionário na vertical
# for i in dicionario_sistema.keys():#vertical
#     print(i).

    
# COM OS DEBUGS:

lista_nome = []
lista_telefone = []
lista_email = []
#adicionar tudo em um dicionário
dicionario_sistema={
    "nomes": lista_nome,
    "telefone": lista_telefone,
    "email": lista_email
}
while True:
    #input nome,telefone,email
    nome_x = str(input("Digite o nome: "))
    lista_nome.append(nome_x)
    telefone = int(input("Digite o telefone: "))
    lista_telefone.append(telefone)
    email = input("Digite o e-mail: ")
    lista_email.append(email)
    
    print(f""" Nome: {nome_x} Telefone: {telefone} E-mail: {email} Cadastrados com sucesso!""")
    
    continuar_x = str(input("digite 's' para sair ou qualquer tecla para continuar: ")).lower()
    if continuar_x == "s":
        print(f"{dicionario_sistema}")
        print("Saindo do sistema...")
        break
#exibir dicionário na vertical
for i in dicionario_sistema.keys():#vertical
    print(i)
    
