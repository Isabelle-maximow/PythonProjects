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