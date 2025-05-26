
def main(dados):
    nome = dados["name"]
    alt = dados["height"]
    peso = dados["weight"]
    print(f'pokemon: {nome.title()}') # .title () primeira letra maiuscula
    print(f'Peso: {peso} kg')
    print(f'Altura: {alt/10} cm')