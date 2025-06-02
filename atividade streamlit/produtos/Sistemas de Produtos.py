from whole1.py import conectar_bd, validar_nome_produto, validar_preco, validar_estoque

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