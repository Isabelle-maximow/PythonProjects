# Sistema Integrado de Cadastro: Alunos, Produtos e Usuários
# Finalidade: Reunir funcionalidades em um único sistema com validações e organização

# MÓDULO: LANÇAR NOTA ALUNO
def validar_nome_aluno():
    while True:
        nome = input("Digite nome e sobrenome do aluno (mínimo 3 letras): ")
        if len(nome) >= 3:
            return nome
        print("Nome inválido. Tente novamente.")

def validar_notas():
    notas = []
    for i in range(4):
        while True:
            nota = float(input(f"Digite a nota {i + 1} (de 0 a 10): "))
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            print("Nota fora do intervalo permitido.")
    return notas

def cadastrar_alunos():
    alunos = []
    while True:
        nome = validar_nome_aluno()
        notas = validar_notas()
        media = sum(notas) / len(notas)
        status = "Aprovado" if media >= 7 else "Reprovado"
        alunos.append([nome, notas, media, status])
        continuar = input("Deseja sair? (s para sim): ").lower()
        if continuar == "s":
            print("Encerrando o sistema cadastrar alunos...")
            break
    return alunos

def exibir_alunos(alunos):
    for aluno in alunos:
        print(f"""
        Nome: {aluno[0]}
        Notas: {aluno[1]}
        Média: {aluno[2]:.2f}
        Situação: {aluno[3]}""")

# MÓDULO: LANÇAR NOTA DE PRODUTO
def validar_nome_produto():
    while True:
        nome = input("Nome do produto (mínimo 3 letras): ")
        if len(nome) >= 3:
            return nome
        print("Nome inválido. (mínimo 3 letras)")

def validar_codigo_produto():
    while True:
        cod = input("Código do produto (4 dígitos): ")
        if len(cod) == 4:
            return cod
        print("Código inválido. Deve ter exatamente 4 dígitos.")

def validar_preco():
    while True:
        preco = float(input("Preço do produto (maior que 0.0 R$): "))
        if preco > 0:
            return preco
        print("Preço inválido.")

def cadastrar_produto():
    produtos = []
    while True:
        nome = validar_nome_produto()
        cod = validar_codigo_produto()
        preco = validar_preco()
        produtos.append([produto, cod, preco])
        continuar = input("Deseja sair? (s para sair): ").lower()
        if continuar == "s":
            print("Encerrando o sistema cadastrar produto.")
            break
    return produtos

def exibir_produtos(produtos):
    for i, prod in enumerate(produtos, start=1):
        print(f"Produto {i}:")
        print(f"""     Código: {prod[1]}
        Nome: {prod[0]}
        Valor: R${prod[2]:.2f}""")

# MÓDULO: CICLO DE USUÁRIOS
usuarios = {
    'nomes': [],
    'emails': []
}

def carregar_dados():
    with open("usuarios.txt", "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")
            nome = dados[0].replace("\n", "")
            telefone = dados[1].replace("\n", "")
            email = dados[2].replace("\n", "")
            usuarios['nomes'].append(nome)
            usuarios['emails'].append(email)

def salvar_dados():
    with open("usuarios.txt", "w") as arquivo:
        for i in range(len(usuarios['nomes'])):
            arquivo.write(f"{usuarios['nomes'][i]};{usuarios['emails'][i]}\n")

def crud_usuarios():
    carregar_dados()
    while True:
        menu = """Menu CRUD:
        1 - Cadastrar usuário
        2 - Visualizar usuário
        3 - Deletar usuário
        4 - Sair e salvar
        Escolha: """

        if menu == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("E-mail: ")
            usuarios['nomes'].append(nome)
            usuarios['emails'].append(email)
            print("Usuário cadastrado com sucesso!")
            
        elif menu == "2":
            if usuarios["nomes"]:
                for i in range(len(usuarios["nomes"])):
                    print(f"""
                        Nome: {usuarios['nomes'][i]},
                        Telefone: {usuarios['tel'][i]},
                        E-mail: {usuarios['emails'][i]}""")
            else:
                print("Nenhum usuário cadastrado.")

        elif menu == "3":
            nome = input("Digite o nome para excluir: ")
            if nome in usuarios ["nome"]:
                idx = usuarios["nome").index(nome)
                for key in usuarios:
                    usuarios [key].pop(idx)
                print("Usuário excluído.")
            else:
                print("Usuário não encontrado.")

        elif menu == "4":
            salvar_dados()
            print("Dados salvos. Encerrando...")
            break
        else:
            print("Opção inválida.")

# SISTEMA INTEGRADO PRINCIPAL
def main():
    while True:
        escolha = input("""
                SISTEMA INTEGRADO:
                1 - Cadastro de Alunos
                2 - Cadastro de Produtos
                3 - Gerenciar Usuários (CRUD)
                4 - Sair do sistema
                Escolha uma opção: """)

        if escolha == "1":
            alunos = cadastrar_alunos()
            exibir_alunos(alunos)

        elif escolha == "2":
            produtos = cadastrar_produto()
            exibir_produtos(produtos)

        elif escolha == "3":
            crud_usuarios()

        elif escolha == "4":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")


# Execução principal protegida com try/except
if __name__ == "__main__":
    try:
        main()
        
    except KeyboardInterrupt:
        print("\nSistema interrompido pelo usuário.")
    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")

