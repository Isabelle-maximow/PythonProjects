
def loop(feriados):
    print("Lista de Feriados Nacionais - 2025:")
    print("-" * 40)
    for feriado in feriados:
        print(f"Nome: {feriado['name']}")
        print(f"Data: {feriado['date']}")
        print(f"Tipo: {feriado['type']}")
        print("-" * 40)
        