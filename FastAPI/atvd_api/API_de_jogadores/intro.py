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


