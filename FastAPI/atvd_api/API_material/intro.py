#API-2
from fastapi import FastAPI
app = FastAPI()
# Simulando uma "base de dados" em memória com uma lista
items = [
    {"id": 1, "nome": "Caneta"},
    {"id": 2, "nome": "Lápis"},
    {"id": 3, "nome": "Borracha"},
    {"id": 4, "nome": "Apontador"},
    {"id": 5, "nome": "Lapiseira"},
    {"id": 6, "nome": "Post-it"},
    {"id": 7, "nome": "Caderno"},
    {"id": 8, "nome": "Folha"},
    {"id": 9, "nome": "Fichário"},
    {"id": 10, "nome": "Régua"}
]
# Endpoint GET para listar todos os itens
@app.get("/")
async def listar_itens():
    return items

# Endpoint GET para pegar um item específico por ID
@app.get("/itens/{item_id}")
async def pegar_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    return {"mensagem": "Item não encontrado"}

# python -m uvicorn API_de_jogadores.intro:app --reload