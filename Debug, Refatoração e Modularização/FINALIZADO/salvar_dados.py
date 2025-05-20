usuarios = {
    'nomes': [],
    'emails': [],
    'telefones': []
}

def salvar_dados():
    try:
        with open("usuarios.txt", "w") as arquivo:
            for nome, email in zip(usuarios.get('nomes', []), usuarios.get('emails', [])):
                arquivo.write(f"{nome};{email}\n")
                
    except IOError: # Verifica se houve erro ao abrir o arquivo
        print("Erro ao acessar o arquivo. Verifique as permissões ou o caminho do arquivo.")
    except Exception as e:  # Captura qualquer outro erro inesperado
        print(f"Ocorreu um erro inesperado: {e}")
    finally:
        print("Operação de salvar dados concluída.")