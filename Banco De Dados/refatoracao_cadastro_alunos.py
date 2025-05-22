
def validar_nome():
    while True:
        nome = input("Digite o nome do aluno: ")
        if len(nome) >= 5:
            return nome
        else: 
            print ("Nome deve ter pelo menos 5 caracteres!")
            
def validar_nota():
    notas = []
    for i in range (1,3):
        nota = float(input(f"Digite a nota {i} entre 0 a 10: "))
        if nota == 0 or nota <= 10:
            notas.append(nota)
            break
        else:
            print("Nota inválida. Deve estar entre 0 e 10!")
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
        continuar = input("Digite "S" para sair ou qualquer tecla para continuar").lower()
        if continuar == "S":
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
                  Médoa: {i["Media"]}
                  Situação: {i["Situação"]}
                  """)
            print("-"*30)
            
    