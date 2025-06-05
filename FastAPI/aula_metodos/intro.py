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

# endpoint para pesquisar por time, método query
@app.get("/get-jogador-time")
def get_jogador_time(time:str):
    # loop para percorrer todos os dados de jogadores:
    for i in jogadores:
        # if para verificar a cpnsulta "query" com o dicionario:
        if jogadores[i]["time"] == time:
            return jogadores[i]
    return {"Dados": "Não foi encontrado"}
# basemodel1 para manipulação de dados do tipo str, float e int 
class Jogador(BaseModel):
    nome: str
    idade: int
    time: str
    
# METODO POST // ENVIAR OS DADOS A UM SERVIDOR VIA API 
# cadastrar jogador:
@app.post("/cadastrar-jogador/{jogador_id}")
def cadastrar_jogador(jogador_id: int, jogador: Jogador):
    # if para verificar jogador exitente:
    if jogador_id in jogadores:
        return{"Erro": "Jogador ja cadastrado!"}
    jogadores[jogador_id] = jogador
    
# METODO PUT // ATUALIZAR UM JOGADOR
# criar um objeto para substituir os dados do jogador - usando o Optional
class AtualizarJogador(BaseModel):
    nome: Optional[str] = None
    idade: Optional[int] = None
    time: Optional[str] = None
    
# endpoint put:
@app.put(";atualizar-jogador/{jogador_id}")
def atualizar_jogador(jogador_id: int, jogador: AtualizarJogador):
    # if para cada situação:
    # se o jogador n existir:
    if jogador_id not in jogadores:
        return{"Erro": "Jogador não cadastrado"}
    # nome
    if jogador.nome != None:
        # add nome do jogador:
        jogadores[jogador_id]["nome"] = jogador.nome
    # idade
    if jogador.idade != None:
        jogadores[jogador_id]["idade"] = jogador.idade
    # time
    if jogador.time != None:
        jogadores[jogador_id]["time"] = jogador.time
        
    return jogadores[jogador_id]

# METODO DELET
@app.delete("/exclusao-jogador/{jogador_id}")
def excluir_jogador(jogador_id:int):
    if jogador_id not in jogadores:
        return{"Erro": "Jogador não cadastrado"}
    # deletar o jogador:
    del jogadores [jogador_id]
    return {"mensagem": "jogador excluido com sucesso"}
    