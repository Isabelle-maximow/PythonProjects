from salvar_dados import salvar_dados
from carregar_dados import carregar_dados
from crud_usuarios import crud_usuarios

def main():
    print("Bem-vindo ao sistema de gerenciamento de usuários!")
    crud_usuarios()
    salvar_dados()
    carregar_dados()
   
if __name__ == "__main__":
    main()