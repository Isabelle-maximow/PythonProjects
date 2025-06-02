import sqlite3
import streamlit as st
# Nome do banco de dados
BANCO_DE_DADOS = "produtos.db"

# Função para conectar ao banco e criar a tabela de produtos
def conectar_bd():
    conexao = sqlite3.connect(BANCO_DE_DADOS)
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            estoque INTEGER NOT NULL)''')
    conexao.commit()
    return conexao, cursor

# Função para validar o nome do produto
def validar_nome_produto():
    while True:
        nome = input("Digite o nome do produto: ").strip()
        if len(nome) >= 3:
            return nome
        else:
            print("Nome inválido. Deve ter pelo menos 3 caracteres.")

# Função para validar o preço do produto
def validar_preco():
    while True:
        try:
            preco = float(input("Digite o preço do produto (ex: 19.99): "))
            if preco > 0:
                return preco
            else:
                print("O preço não pode ser negativo.")
        except:
            print("Erro: Digite um número válido.")

# Função para validar a quantidade em estoque
def validar_estoque():
    while True:
        try:
            estoque = int(input("Digite a quantidade em estoque: "))
            if estoque >= 0:
                return estoque
            else:
                print("O estoque não pode ser negativo.")
        except ValueError:
            print("Erro: Digite um número inteiro.")

# Função Cadastrar produto
def cadastrar_produto():
    conexao, cursor = conectar_bd()
    nome = validar_nome_produto()
    preco = validar_preco()
    estoque = validar_estoque()
    cursor.execute("INSERT INTO produtos (nome, preco, estoque) VALUES (?, ?, ?)",
                   (nome, preco, estoque))
    conexao.commit()
    conexao.close()
    print("Produto cadastrado com sucesso!")

# Função Exibir todos os produtos
def exibir_produtos():
    conexao, cursor = conectar_bd()
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    conexao.close()
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        for produto in produtos:
            print(f"ID: {produto[0]}")
            print(f"Nome: {produto[1]}")
            print(f"Preço: R${produto[2]:.2f}")
            print(f"Estoque: {produto[3]}")
            print("-" * 30)

# Função - Atualizar produto
def atualizar_produto():
    exibir_produtos()
    conexao, cursor = conectar_bd()
    while True:
        try:
            id_produto = int(input("Digite o ID do produto para atualizar (ou 0 para cancelar): "))
            if id_produto == 0:
                print("Operação cancelada.")
                break
            cursor.execute("SELECT id FROM produtos WHERE id = ?", (id_produto,))
            if cursor.fetchone():
                nome = validar_nome_produto()
                preco = validar_preco()
                estoque = validar_estoque()
                cursor.execute("UPDATE produtos SET nome = ?, preco = ?, estoque = ? WHERE id = ?",
                               (nome, preco, estoque, id_produto))
                conexao.commit()
                print("Produto atualizado com sucesso!")
                break
            else:
                print("ID inválido. Tente novamente.")
        except ValueError:
            print("Erro: Digite um número válido.")
    conexao.close()

# Função - Deletar produto
def deletar_produto():
    exibir_produtos()
    conexao, cursor = conectar_bd()
    while True:
        try:
            id_produto = int(input("Digite o ID do produto para deletar (ou 0 para cancelar): "))
            if id_produto == 0:
                print("Operação cancelada.")
                break
            cursor.execute("SELECT id FROM produtos WHERE id = ?", (id_produto,))
            if cursor.fetchone():
                cursor.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))
                conexao.commit()
                print("Produto deletado com sucesso!")
                break
            else:
                print("ID inválido. Tente novamente.")
        except ValueError:
            print("Erro: Digite um número válido.")
    conexao.close()



# Menu principal
def menu():
    # fica em cima (indicador de pag)
    st.set_page_config(page_title="Sistema de Produtos.py", page_icon="📦")
    st.title("Sistema de Gerenciamento de Produtos")
    
    # sidebar
    st.sidebar.title("Menu")
    st.sidebar.header("Selecione o que deseja fazer")

    with st.sidebar:
        if st.button("Cadastrar produtos", use_container_width=True):
            st.session_state.page = cadastrar_produto()  


        
        # print("\nSistema de Gerenciamento de Produtos")
        # print("1. Cadastrar produto")
        # print("2. Exibir todos os produtos")
        # print("3. Atualizar produto")
        # print("4. Deletar produto")
        # print("5. Sair")
        # opcao = input("Escolha uma opção (1-5): ")
        # if opcao == "1":
        #     cadastrar_produto()
        # elif opcao == "2":
        #     exibir_produtos()
        # elif opcao == "3":
        #     atualizar_produto()
        # elif opcao == "4":
        #     deletar_produto()
        # elif opcao == "5":
        #     print("Saindo do sistema...")
        #     break
        # else:
        #     print("Opção inválida. Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    menu()
