from fastapi import FastAPI
app = FastAPI(title="API de Produtos")
produtos = [
    {"id": 1, "nome": "Notebook", "preco": 3500.00},
    {"id": 2, "nome": "Smartphone", "preco": 2000.00},
    {"id": 3, "nome": "Fone de Ouvido", "preco": 150.00}
]
# Endpoint GET para listar todos os produtos
@app.get("/produtos/")
async def listar_produtos():
    # Retorna a lista completa de produtos
    return produtos
# Endpoint GET para pegar um produto por ID
@app.get("/produtos/{produto_id}")
async def pegar_produto(produto_id: int):
    # loop sobre a lista de produtos para encontrar o ID
    for produto in produtos:
        if produto["id"] == produto_id:
            # Retorna o produto encontrado
            return produto
    # Retorna uma mensagem de erro se o produto não for encontrado
    return {"mensagem": f"Produto com ID {produto_id} não encontrado"}