
def validar_nome():
    while True:
        nome = input("Digite o nome do aluno: ")
        if len(nome) >= 5:
            return nome
        else: 
            print ("Nome deve ter pelo menos 5 caracteres!")
            
def validar_nota():
    notas = []
    for i in range(1, 4):
        while True:
            try:
                nota = float(input(f"Digite a nota {i} entre 0 a 10: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Nota inválida. Deve estar entre 0 e 10!")
            except ValueError:
                print("Por favor, digite um número válido.")
    return notas

def calculo_media(notas):
    media = sum (notas)/len(notas)
    situacao = "Aprovado" if media >= 6 else "Reprovado"
    return media, situacao
    
def cadastro_aluno(alunos):
    while True:
        nome = validar_nome()
        notas = validar_nota()
        media, situacao = calculo_media(notas)
        
        # add em um dicionario:
        alunos.append({
            "Nome": nome,
            "Notas": notas,
            "Media": media,
            "Situação": situacao
        })
        
        # encontrar sistema ou sair 
        continuar = input("Digite 's' para sair ou qualquer tecla para continuar: ").lower()
        if continuar == "s":
            print("Saindo do sistemas...")
            break
        
def exibir_aluno(alunos):
    if not alunos: # se n tiver alunos cadastrados
        print("Nenhum aluno cadastrado...")
    else:
        for i in alunos:
            print("-"*30)
            print(f""" 
                  Nome: {i["Nome"]}
                  Notas: {i["Notas"]}
                  Média: {i["Media"]}
                  Situação: {i["Situação"]}
                  """)
            print("-"*30)
            

def editar_aluno(alunos):
    nome = input("Digite o nome do aluno que deseja editar: ").lower()
    for i in alunos: # loop para verificar o nome do input na lista
        if i ["nome"].lower() == nome:
            print (f"Notas atuais: {i["Notas"]}")
            novas_notas = validar_nota()
            media, situacao = calculo_media(novas_notas)
            # add no dicionario :
            {i["Notas"]} == novas_notas
            {i["Media"]} == media
            {i["Situação"]} == situacao
            
            print(f"Notas do aluno {i["nome"]} atualizadas com sucesso!")
        
        else:
            print(f"Nome do aluno: {nome} não encontradi.")
            
# alunos aprovados e reprovados:
# criando filtro 
def exibir_situacao(alunos, situacao):
    # lista para armazenar o filtro dos alunos 
    filtros = [
        # loop para exibir a situação:
        i for i in alunos
        # if p puxar a chave "Situação" do dicionario:
        if i["Situação"] == situacao ]
    
    # exibir quando n tem alunos:
    if not filtros:
        print("Nenhum aluno encontrado!")
    else:
        for i in filtros:
            print(f"Nome:{i["nome"]}, Situação:{i["Situação"]} ")
            
            
def menu():
    print(""" Menu de Opções
          1 - Cadastrar alunos.
          2 - Exibir alunos.
          3 - Editar as notas de um aluno.
          4 - Exibir alunos aprovados.
          5 - Exibir alunos reprovados.
          6 - Sair do sistema
          """)
    opcao = input("Escolha uma opção: ")
    return opcao

def main():
    alunos = []
    while True:
        opcao = menu()
        if opcao == "1":
            cadastro_aluno(alunos)
        elif opcao == "2":
            exibir_aluno(alunos)
        elif opcao == "3":
            editar_aluno(alunos)
        elif opcao == "4":
            exibir_situacao(alunos, "Aprovado")
        elif opcao == "5":
            exibir_situacao(alunos, "Reprovado")
        elif opcao == "6":
            print("Saindo do sistemas...")
        else:
            print("Opção inválida, escolha uma opção existente.")
            
if __name__ == "__main__":
    main()                
    