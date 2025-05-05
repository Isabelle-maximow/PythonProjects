# refaturar o cod/ atualizar o cod
# sistema smp precisa de update 
# CRUD básico
# Create - Read - Update - Delete

# RELACIONADO A ATVD 1
lista_nomes = []
lista_emails = []
lista_telefones = []
# add em um dicionario
dicionario_sys = {
    'nome': lista_nomes,
    'email': lista_emails,
    'telefone': lista_telefones
}
while True:
    # menu de opções
    menu = input("""
                 Menu:
                    1 - Cadastrar Cliente
                    2 - Visualizar Clientes
                    3 - Deletar Cliente
                    4 - Sair e salvar em um .txt
                    Escolha uma opção: """)
    # opção 1 - cadastrar cliente:
    if menu == '1':
        nome_x = input('Digite o nome: ')
        lista_nomes.append(nome_x)
        email_x = input('Digite o e-mail: ')
        lista_emails.append(email_x)
        telefone_x = input('Digite o telefone: ')
        lista_telefones.append(telefone_x)
        
        print(f""" 
              Nome: {nome_x} 
              Telefone: {telefone_x} 
              E-mail: {email_x} 
              Cadastrados com sucesso!""")
    # opção 2 - visualizar clientes:
    elif menu == '2':
        # se tiver usuario cadastrado:
        if lista_nomes:
            print('Clientes cadastrados:')
            # loop para mostrar na vertical
            for i in range(len(lista_nomes)):
                print(f""" 
                    Nome: {lista_nomes[i]} 
                    Telefone: {lista_telefones[i]} 
                    E-mail: {lista_emails[i]} """)
        # nenhum cliente cadastrado:
        else:
            print('Nenhum cliente cadastrado.')
    # opção 3 - deletar cliente:
    # opcao 4 - Sair:
    elif menu == '4':
        print('Saindo do Sistema...')
        break
    else:
        print('Opção inválida. Tente novamente.')
    