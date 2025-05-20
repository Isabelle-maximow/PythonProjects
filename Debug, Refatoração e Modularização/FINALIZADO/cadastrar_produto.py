from validar_preco import validar_preco
from validar_cod_produto import validar_codigo_produto
from validar_nome_produto import validar_nome_produto

def cadastrar_produto():
    produtos = []
    while True:
        try:
            nome = validar_nome_produto()
            cod = validar_codigo_produto()
            preco = validar_preco()
            produtos.append([nome, cod, preco])
            continuar = input("Deseja sair? (s para sair): ").lower()
            if continuar == "s":
                print("Encerrando o sistema cadastrar produto.")
                return produtos
                
        except Exception as erro:
            print(f"Erro inesperado: {erro}")
        except ValueError:
            print("Erro: Valor inválido.")
            
        finally:
            print("Produto cadastrado com sucesso!")
            print(f"Produto: {nome}")
            print(f"Código: {cod}")
            print(f"Preço: R${preco:.2f}")