
def filtros(dados):
    for habilidade in dados["abilities"]:
        print(f'Habilidades: {habilidade["ability"]["name"]}')