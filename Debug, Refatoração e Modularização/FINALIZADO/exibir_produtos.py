
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