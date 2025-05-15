import streamlit as st

# cadastro de produto
# lista produtos:
produto = []

# titulo da aplicação web:
st.title("Cadastro de Produtos")

# subtitulo com instruções:
st.subheader("Preencha os campos abaixo para cadastrar um produto:")

# função para validar o produto:
def validar_nome(nome):
    return len(nome) >= 3

# função para validar o código do produto:
def validar_cod(codigo):
    return len(codigo) == 4 and codigo.isdigit() # verificar se foi digitado numeros ou str 

# fubção para validar preço do produto:
def validar_preco(preco):
    try:
        return preco > 0.0
    except ValueError:
        return False
    
# formulario de entrada de dados - com with para criar o formulario:
with st.form(key = "form_produto"):
    nome = st.text_input("Nome do Produto: ") # campo de texto
    codigo = st.text_input("Código do Produto: ") 
    preco = st.number_input("Preço do Produto: ", min_value = 0.0, step = 0.01) # valor minimo (maximo seria: 'max_value = ' step é a razão q vai subinddo o num
    
    # botão para enviar o formulario:
    enviar = st.form_submit_button("Cadastrar Produto")
    
    if enviar:
        # validar os dados:
        if not validar_nome(nome):
            st.error("Nome inválido! O nome deve ter pelo menos 3 caracteres.") # mensagem de erro
        elif not validar_cod(codigo):
            st.error("Código inválido! O código deve ter exatamente 4 dígitos.")
        elif not validar_preco(preco):
            st.error("Preço inválido! O preço deve ser um número positivo.")
        else:
            # adicionar o produto a lista:
            produto.append({"nome": nome, "codigo": codigo, "preco": preco})
            st.success("Produto cadastrado com sucesso!")