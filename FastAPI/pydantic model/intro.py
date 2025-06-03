
# pydantic model para lidar com os dados 
# typing dados
# pip install pydantic
# pip install typing
from fastapi import FastAPI
from pydantic import BaseModel # metodo get, put, post e delete
from typing import Optional # requisição de dados da API

app = FastAPI(title = "FastApi")

# coleção de dicionario como base de dados para requiisição 
jogadores = {
    1: {"nome": "Ronaldo", "Idade": "23", "Time": "Brasil"},
    2: {"nome": "Messi", "Idade": "36", "Time": "Argentina"},
    3: {"nome": "Mbappé", "Idade": "25", "Time": "França"},
    4: {"nome": "Modric", "Idade": "38", "Time": "Croácia"},
    5: {"nome": "Kane", "Idade": "30", "Time": "Inglaterra"},
    6: {"nome": "Vinícius Jr", "Idade": "24", "Time": "Brasil"}
}

# criar endpoints get:
@app.get("/") # endpoint raiz
def inicio():
    return jogadores 

# endpoint trazer jogador pelo id:
@app.get("/get-jogador/{id_jogador}")
def get_jogador(id_jogador: str):
    return jogadores[id_jogador]
    