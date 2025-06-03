'''
FastAPI é um framework web moderno para construir APIs
(interfaces de programação de aplicações) em Python. Foco em alta performance,
facilidade de uso e produtividade. Ele é especialmente útil para criar APIs
RESTful (um estilo comum de APIs para comunicação entre sistemas) de
maneira rápida e eficiente.

Principais características do FastAPI:

Alta Performance>>
Baixo nível de complexidade, que é adequado para construir
serviços web assíncronos, está no  mesmo nível de performance de linguagens como
Node.js e Go.

Uso de Type Hints>>
O FastAPI aproveita as anotações de tipo do Python (ex.: str, int, List)
para validar dados automaticamente e gerar documentação interativa.
Isso reduz erros e te poupa tempo.

Programação Assíncrona>>
Com suporte a async e await, ele é ideal para aplicações que precisam lidar com
muitas requisições simultâneas, como chamadas a bancos de dados ou serviços
externos.

Documentação Automática>>
Ao criar uma API, o FastAPI gera automaticamente uma interface interativa
(usando Swagger UI ou ReDoc) onde você pode testar seus endpoints sem
precisar de ferramentas extras.

Facilidade de Uso>>
Mesmo sendo poderoso, o código é simples e intuitivo, especialmente se você já
conhece Python. Ele elimina muita configuração manual que frameworks como Flask
exigem.

Validação de Dados com Pydantic>>
O FastAPI usa o Pydantic, uma biblioteca que valida e converte dados
automaticamente com base nos tipos que você define. Isso significa menos
código para checar entradas manualmente.
'''

# pip install fastapi uvicorn
from fastapi import FastAPI

# criar uma instancia do fastapi = subir a aplicação: 
app = FastAPI() # instancia do app API 

# definir um endpoint simples = basicmanete, é uma ponte/caminho da API:
@app.get("/") # @app.get define o endpoint metodo get na raiz (/) | ele é tmb um decorator (decorar o caminho)

# definir uma função async:
async def raiz(): # async def: usa programação assincrona: n tem ordem, oq chegae primeiro vai, isso traz mais agilidade e rapidez(requisição mais rapida)
    return{"mensagem": "Olá mundo!"}

# endpoint com parametro type hint = str 
@app.get("/saudacao/{nome}")
async def saudacao(nome: str):
    return{"mensagem": f"Olá, {nome}"}

# rodar API uvicorn:
# python -m uvicorn main: nome_arquivo_sem.py --reload 
# python -m uvicorn main: intro --reload 
