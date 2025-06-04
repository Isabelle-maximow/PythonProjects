from fastapi import FastAPI
# Cria uma instância do FastAPI com um título
app = FastAPI(title="API de Livros")
# Dicionário em memória simulando uma base de dados de livros
livros = {
    # Filosofia
    1: {"titulo": "Assim Falou Zaratustra", "autor": "Friedrich Nietzsche", "ano": 1883, "ID": 1},
    2: {"titulo": "Além do Bem e do Mal", "autor": "Friedrich Nietzsche", "ano": 1886, "ID": 2},
    3: {"titulo": "O Mundo como Vontade e Representação", "autor": "Arthur Schopenhauer", "ano": 1818, "ID": 3},
    4: {"titulo": "Meditações", "autor": "Marco Aurélio", "ano": 180, "ID": 4},
    5: {"titulo": "A República", "autor": "Platão", "ano": -380, "ID": 5},
    6: {"titulo": "Ética a Nicômaco", "autor": "Aristóteles", "ano": -340, "ID": 6},
    7: {"titulo": "Discurso do Método", "autor": "René Descartes", "ano": 1637, "ID": 7},
    8: {"titulo": "O Contrato Social", "autor": "Jean-Jacques Rousseau", "ano": 1762, "ID": 8},
    9: {"titulo": "O Ser e o Nada", "autor": "Jean-Paul Sartre", "ano": 1943, "ID": 9},
    10: {"titulo": "O Segundo Sexo", "autor": "Simone de Beauvoir", "ano": 1949, "ID": 10},
    11: {"titulo": "A Náusea", "autor": "Jean-Paul Sartre", "ano": 1938, "ID": 11},
    12: {"titulo": "O Mito de Sísifo", "autor": "Albert Camus", "ano": 1942, "ID": 12},
    13: {"titulo": "O Estrangeiro", "autor": "Albert Camus", "ano": 1942, "ID": 13},
    14: {"titulo": "Crítica da Razão Pura", "autor": "Immanuel Kant", "ano": 1781, "ID": 14},
    15: {"titulo": "Dialética do Esclarecimento", "autor": "Adorno e Horkheimer", "ano": 1944, "ID": 15},

    # Romance clássico internacional
    16: {"titulo": "Guerra e Paz", "autor": "Leon Tolstói", "ano": 1869, "ID": 16},
    17: {"titulo": "Anna Kariênina", "autor": "Leon Tolstói", "ano": 1877, "ID": 17},
    18: {"titulo": "Os Miseráveis", "autor": "Victor Hugo", "ano": 1862, "ID": 18},
    19: {"titulo": "O Conde de Monte Cristo", "autor": "Alexandre Dumas", "ano": 1844, "ID": 19},
    20: {"titulo": "Os Três Mosqueteiros", "autor": "Alexandre Dumas", "ano": 1844, "ID": 20},
    21: {"titulo": "Jane Eyre", "autor": "Charlotte Brontë", "ano": 1847, "ID": 21},
    22: {"titulo": "O Morro dos Ventos Uivantes", "autor": "Emily Brontë", "ano": 1847, "ID": 22},
    23: {"titulo": "Orgulho e Preconceito", "autor": "Jane Austen", "ano": 1813, "ID": 23},
    24: {"titulo": "Razão e Sensibilidade", "autor": "Jane Austen", "ano": 1811, "ID": 24},
    25: {"titulo": "Emma", "autor": "Jane Austen", "ano": 1815, "ID": 25},
    26: {"titulo": "Drácula", "autor": "Bram Stoker", "ano": 1897, "ID": 26},
    27: {"titulo": "Frankenstein", "autor": "Mary Shelley", "ano": 1818, "ID": 27},
    28: {"titulo": "Madame Bovary", "autor": "Gustave Flaubert", "ano": 1857, "ID": 28},
    29: {"titulo": "O Retrato de Dorian Gray", "autor": "Oscar Wilde", "ano": 1890, "ID": 29},
    30: {"titulo": "David Copperfield", "autor": "Charles Dickens", "ano": 1850, "ID": 30},
    31: {"titulo": "Grandes Esperanças", "autor": "Charles Dickens", "ano": 1861, "ID": 31},
    32: {"titulo": "O Amante de Lady Chatterley", "autor": "D.H. Lawrence", "ano": 1928, "ID": 32},

    # Romance clássico nacional
    33: {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899, "ID": 33},
    34: {"titulo": "Memórias Póstumas de Brás Cubas", "autor": "Machado de Assis", "ano": 1881, "ID": 34},
    35: {"titulo": "Quincas Borba", "autor": "Machado de Assis", "ano": 1891, "ID": 35},
    36: {"titulo": "A Moreninha", "autor": "Joaquim Manuel de Macedo", "ano": 1844, "ID": 36},
    37: {"titulo": "Senhora", "autor": "José de Alencar", "ano": 1875, "ID": 37},
    38: {"titulo": "Iracema", "autor": "José de Alencar", "ano": 1865, "ID": 38},
    39: {"titulo": "Lucíola", "autor": "José de Alencar", "ano": 1862, "ID": 39},
    40: {"titulo": "O Primo Basílio", "autor": "Eça de Queirós", "ano": 1878, "ID": 40},
    41: {"titulo": "A Cidade e as Serras", "autor": "Eça de Queirós", "ano": 1901, "ID": 41},
    42: {"titulo": "O Mulato", "autor": "Aluísio Azevedo", "ano": 1881, "ID": 42},
    43: {"titulo": "O Cortiço", "autor": "Aluísio Azevedo", "ano": 1890, "ID": 43},
    44: {"titulo": "Vidas Secas", "autor": "Graciliano Ramos", "ano": 1938, "ID": 44},
    45: {"titulo": "São Bernardo", "autor": "Graciliano Ramos", "ano": 1934, "ID": 45},
    46: {"titulo": "A Hora da Estrela", "autor": "Clarice Lispector", "ano": 1977, "ID": 46},
    47: {"titulo": "Perto do Coração Selvagem", "autor": "Clarice Lispector", "ano": 1943, "ID": 47},
    48: {"titulo": "O Tempo e o Vento", "autor": "Erico Verissimo", "ano": 1949, "ID": 48},
    49: {"titulo": "Incidente em Antares", "autor": "Erico Verissimo", "ano": 1971, "ID": 49}
}


# Endpoint GET para a raiz, retorna todos os livros
@app.get("/")
async def listar_livros():
    return livros

# Endpoint GET para pegar um livro específico por ID
@app.get("/livros/{livro_id}")
async def pegar_livro(livro_id: int):
    # Verifica se o ID existe no dicionário
    if livro_id in livros:
        # Retorna o livro correspondente ao ID
        return livros[livro_id]
    # Retorna uma mensagem de erro se o livro não for encontrado
    return {"mensagem": f"Livro com ID {livro_id} não encontrado"}