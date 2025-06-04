import requests
from fastapi import FastAPI

#path parameter
app = FastAPI()
#lista de jogadores
jogadores = {
    1: {
        "nome": "Ronaldo",
        "idade": 28,
        "time": "Brasil"
    },
    2: {
        "nome": "Rodrygo",
        "idade": 29,
        "time": "Real Madrid"
    },
    3: {
        "nome": "Messi",
        "idade": 36,
        "time": "Inter Miami"
    },
    4: {
        "nome": "Mbappé",
        "idade": 25,
        "time": "Paris Saint-Germain"
    },
    5: {
        "nome": "Neymar",
        "idade": 32,
        "time": "Al-Hilal"
    },
    6: {
        "nome": "Vinícius Jr",
        "idade": 24,
        "time": "Real Madrid"
    },
    7: {
        "nome": "Modric",
        "idade": 38,
        "time": "Real Madrid"
    },
    8: {
        "nome": "Kanté",
        "idade": 33,
        "time": "Al-Ittihad"
    },
    9: {
        "nome": "Cristiano Ronaldo",
        "idade": 39,
        "time": "Al-Nassr"
    },
    10: {
        "nome": "Haaland",
        "idade": 23,
        "time": "Manchester City"
    }
}

# Cria uma instância do FastAPI com um título
@app.get("/")
def inicio():
    return jogadores

@app.get("/get-jogador/{id_jogador}")
async def get_jogador(id_jogador:int):
    return jogadores[id_jogador]



# ##############################################
# ##############################################
# #API-4
# # Importa o FastAPI para criar a API
# from fastapi import FastAPI

# # Cria uma instância do FastAPI com um título
# app = FastAPI(title="API de Produtos")

# # Lista em memória simulando uma base de dados de produtos
# produtos = [
#     {"id": 1, "nome": "Notebook", "preco": 3500.00},
#     {"id": 2, "nome": "Smartphone", "preco": 2000.00},
#     {"id": 3, "nome": "Fone de Ouvido", "preco": 150.00}
# ]

# # Endpoint GET para listar todos os produtos
# @app.get("/produtos/")
# async def listar_produtos():
#     # Retorna a lista completa de produtos
#     return produtos

# # Endpoint GET para pegar um produto por ID
# @app.get("/produtos/{produto_id}")
# async def pegar_produto(produto_id: int):
#     # loop sobre a lista de produtos para encontrar o ID
#     for produto in produtos:
#         if produto["id"] == produto_id:
#             # Retorna o produto encontrado
#             return produto
#     # Retorna uma mensagem de erro se o produto não for encontrado
#     return {"mensagem": f"Produto com ID {produto_id} não encontrado"}
