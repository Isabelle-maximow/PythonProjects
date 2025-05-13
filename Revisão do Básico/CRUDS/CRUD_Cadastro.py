'''
CRUD de Cadastro com nome, telefone e e-mail
'''

lista_nome = []
lista_telefone = []
lista_email = []

# adicionando os dados em um dicionário
dicionario = {
    "nome": lista_nome,
    "tell": lista_telefone,
    "email": lista_email
}

# função carregar dados ao inicar o programa
def carregar_dados():
    try:
        with open("usuarios.txt", "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(", ")
                
                # estrair os valores apos as chaves
                # replace = cria uma copia do arquivo original sem modificar:
                nome = dados[0].replace("Nome: ", "")
                email = dados[1].replace("E-mail: ", "")
                telefone = dados[3].replace("Telefone: ", "")
                
                # add os dados:
                lista_nome.append(nome)
                lista_telefone.append(telefone)
                lista_email.append(email)  
                
    except FileNotFoundError:
        # se o arquivo não existir, comece uma lista vazia para n parar o programa
        pass

# carregar dados existentes ap iniciar:
carregar_dados() 




# menu de opções
while True:
    menu = input ("""
                MENU:
        1 - Adicionar um usuario
        2 - Visualizar usuario
        3 - Deletar usuario
        4 - Salvar e Sair 
        Escolha uma opção: """)
    # opção 1: 
    if menu == "1":
        nome = str(input("Digite o nome: "))
        lista_nome.append(nome)
        tell = int(input("Digite o telefone: "))
        lista_telefone.append(tell)
        email = str(input("Digite o e-mail: "))
        lista_email.append(email)
        print("Usuario adicionado com sucesso!")
        
        # PRÉ TESTE
        # print(dicionario)
        
    # opção 2:
    elif menu == "2":
        if lista_nome: # se tiver usuarios cadastrados
            print("Usuarios cadastrados:")
            for i in range(len(lista_nome)):
                print(f"Nome: {lista_nome[i]}, Telefone: {lista_telefone[i]}, E-mail: {lista_email[i]}")
        else:
            print("Nenhum usuario cadastrado.")
            
    # opção 3:
    elif menu == "3":
        deletar = str(input("Digite o nome do usuario que deseja deletar: "))
        # se o nome estiver na lista, deletar:
        if deletar in lista_nome:
            # pegar o indice da lista para deletar:
            indice = lista_nome.index(deletar)
            # remover o nome, telefone e email:
            lista_nome.pop(indice)
            lista_telefone.pop(indice)
            lista_email.pop(indice)
            print(f"Usuario {deletar} deletado com sucesso!")
        else:
            print(f"Usuario {deletar} não encontrado.")
    
    # opção 4: salvar em txt
    elif menu == "4":
        with open("usuarios.txt", "w") as arquivo:
            # loop para escrever os dados no arquivo linha por linha
            for i in range(len(lista_nome)):
                arquivo.write(f"Nome: {lista_nome[i]}, Telefone: {lista_telefone[i]}, E-mail: {lista_email[i]}\n")
        print("Saindo...")
        break
    else:
        print("Comando inexistentre")
