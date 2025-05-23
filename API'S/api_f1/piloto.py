def piloto(dados):
    if len(dados) > 0:
        piloto = dados[0]
        print("Informações do Piloto:")
        print(f"Nome: {piloto.get('full_name', 'Desconhecido')}")
        print(f"Equipe: {piloto.get('team_name', 'Não disponível')}")
        print(f"Nacionalidade: {piloto.get('country_code', 'Não informada')}")
        print(f"Número do carro: {piloto.get('driver_number', 'N/A')}")
        print(f"URL da foto: {piloto.get('headshot_url', 'Sem imagem disponível')}")
    else:
        print("Nenhum dado encontrado para esse piloto.")