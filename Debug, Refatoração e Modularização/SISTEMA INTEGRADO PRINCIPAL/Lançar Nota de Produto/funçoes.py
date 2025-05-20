# MÓDULO: LANÇAR NOTA DE PRODUTO
def validar_nome_produto():
    while True:
        try:
            nome = input("Nome do produto (mínimo 3 letras): ").strip()
            if len(nome) >= 3:
                return nome
            else:
                print("Nome inválido. (mínimo 3 letras)")
        except Exception as erro:
            print(f"Erro inesperado: {erro}")

def validar_codigo_produto():
    while True:
        try:
            cod = input("Código do produto (4 dígitos): ")
            if len(cod) == 4 and cod.isdigit(): # esse is_digit() verifica se o código contém apenas dígitos
                return cod
            else:
                print("Código inválido. Deve ter exatamente 4 dígitos.")
                
        except ValueError:
            print("Erro: Código deve conter apenas dígitos.")
        except Exception as erro:
            print(f"Erro inesperado: {erro}")

def validar_preco():
    while True:
        try:
            preco = float(input("Preço do produto (maior que 0.0 R$): "))
            if preco > 0:
                return preco
            else:
                print("Preço inválido.")  
        except ValueError:
            print("Erro: Preço deve ser um número.")
        except Exception as erro:
            print(f"Erro inesperado: {erro}")

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

def exibir_produtos(produtos):
    try:
        for i, prod in enumerate(produtos, start=1):
            print(f"Produto {i}:")
            print(f"""     Código: {prod[1]}
        Nome: {prod[0]}
        Valor: R${prod[2]:.2f}""")
            
    except IndexError:
        print("Erro: Produto com dados incompletos.")
    except TypeError:
        print("Erro: Estrutura de dados inválida.")
    except Exception as erro:
        print(f"Erro inesperado: {erro}")
        
    finally:
        print("Exibição de produtos concluída.")
        print("Sistema de exibição de produtos encerrado.")