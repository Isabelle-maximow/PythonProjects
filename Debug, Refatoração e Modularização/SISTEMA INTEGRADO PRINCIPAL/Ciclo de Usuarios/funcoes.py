
# MÓDULO: CICLO DE USUÁRIOS
usuarios = {
    'nomes': [],
    'emails': [],
    'telefones': []
}

def carregar_dados():
    try:
        with open("usuarios.txt", "r") as arquivo:
            for linha in arquivo:
                try:
                    dados = linha.strip().split(";") #strip() remove espaços em branco no início e no final da string e split(";") divide a string em uma lista
                    nome = dados[0]
                    telefone = dados[1]
                    email = dados[2]
                    usuarios['nomes'].append(nome)
                    usuarios['telefones'].append(telefone)
                    usuarios['emails'].append(email)
                    
                except IndexError: # Verifica se a linha tem o número correto de campos
                    print("Linha inválida no arquivo. Verifique o formato: nome;telefone;email")
                    
    except FileNotFoundError: # Verifica se o arquivo existe
        print("Arquivo 'usuarios.txt' não encontrado. Ele será criado ao salvar os dados.")  

def salvar_dados():
    try:
        with open("usuarios.txt", "w") as arquivo:
            for nome, email in zip(usuarios.get('nomes', []), usuarios.get('emails', [])):
                arquivo.write(f"{nome};{email}\n")
                
    except IOError: # Verifica se houve erro ao abrir o arquivo
        print("Erro ao acessar o arquivo. Verifique as permissões ou o caminho do arquivo.")
    except Exception as e:  # Captura qualquer outro erro inesperado
        print(f"Ocorreu um erro inesperado: {e}")

    

def crud_usuarios():
    carregar_dados()
    while True:
        try:
            menu = input("""Menu CRUD:
            1 - Cadastrar usuário
            2 - Visualizar usuário
            3 - Deletar usuário
            4 - Sair e salvar
            Escolha uma opção: """)
    
            if menu == "1":
                while True:
                    nome = input(" Insira o nome: ")
                    telefone = input("Insira o telefone: ")
                    email = input("Insira o E-mail: ")
                    
                    usuarios['nomes'].append(nome)
                    usuarios['emails'].append(email)
                    usuarios['telefones'].append(telefone)
                    
                    print("Usuário cadastrado com sucesso!")
                    outro = input("Deseja cadastrar outro usuário? (s/n)")
                    if outro != "s":
                        break
                
            elif menu == "2":
                if usuarios["nomes"]:
                 for i in range(len(usuarios["nomes"])):
                     print(f"""
                            Usuário {i + 1}
                            Nome: {usuarios['nomes'][i]}
                            Telefone: {usuarios['telefones'][i]}
                            E-mail: {usuarios['emails'][i]}
                            """)
                else:
                    print("Nenhum usuário cadastrado.")
            elif menu == "3":
                nome = input("Digite o nome para excluir: ")
                if nome in usuarios["nomes"]:
                    idx = usuarios["nomes"].index(nome) # encontra o índice do usuário
                    for key in ["nomes", "telefones", "emails"]: 
                        usuarios[key].pop(idx)  # removendo os dados do usuário
                    print("Usuário excluído com sucesso.")
                else:
                    print("Usuário não encontrado.")

            elif menu == "4":
                salvar_dados()
                print("Dados salvos. Encerrando...")
                break
            else:
                print("Opção inválida.")
        
        except KeyboardInterrupt:
            print("\nOperação cancelada pelo usuário.")
        except ValueError:
            print("Valor inválido. Tente novamente.")
            
        