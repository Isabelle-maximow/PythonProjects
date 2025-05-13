
# primeira função, validar nome do produto a partir de 3 caracteres
def validar_produto():
    while True:
        nome = str(input("Digite o nome do produto: "))	
        if len(nome) >= 3:
            return nome
        else:
            print("Nome inválido. O nome deve ter pelo menos 3 caracteres.")
            continue
    
# segunda função, validar código do produto:
def validar_codigo():
    while True:
        codigo = float(input("Crie um código para o prroduto(4 caraceteres): "))
        if len(codigo) == 4:
            return codigo
        else:
            print("Código inválido. O código deve ter exatamente 4 caracteres.")
            continue

# terceira função, criar a validação do preço:
def validar_preco():
    while True:
        try:
            preco = float(input("Digite o preço do produto: "))
            if preco > 0.0:
                return preco
            else:
                print("Preço inválido. O preço deve ser maior que zero.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
            
# quarta função, cadastro:
def cadastro_produto():
    produtos = []
    # armazenado na lista produtos:
    while True:
        produtos.append({
            "nome": validar_produto(),
            "codigo": validar_codigo(),
            "preco": validar_preco()
        })
        continuar = input("Deseja cadastrar outro produto? (s/n): ").lower()
        if continuar != 's':
            print("Cadastro concluído! Saindo do sistema...")
            break
    return produtos

# quinta função, exibir os produtos cadastrados:
def exibir_produtos(produtos):
    # caso nao tenha o produto:
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        # for para exibir produtos:
        for i in range (len(produtos)):
            print(f"Produto {i+1}° cadastrado")
            print(f"Nome: {produtos[i]['nome']}")
            print(f"Código: {produtos[i]['codigo']}")
            print(f"Preço: {produtos[i]['preco']}")
            
# sexta função, principal:
def main():
    print("Sistema de Cadastro de Produtos")
    produtos = cadastro_produto() # chama a função de cadastro
    exibir_produtos(produtos) # chama a função de exibição

if __name__ == "__main__":
    main() # chama a função principal