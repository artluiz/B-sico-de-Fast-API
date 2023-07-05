from fastapi import FastAPI

app = FastAPI()

invent = {
    1: {"item": "lata", "preco_unitario": 4, "quantidade": 5},
    2: {"item": "garrafa 2L", "preco_unitario": 15, "quantidade": 5},
    3: {"item": "garrafa 750ml", "preco_unitario": 10, "quantidade": 5},
    4: {"item": "lata mini", "preco_unitario": 2, "quantidade": 5},
}

@app.get("/")
def home():
    return {"Inventário": len(invent)}

@app.get("/invent/{id_invent}")
def pegar_venda(id_invent: int):
    if id_invent in invent:
        return invent[id_invent]
    else:
        return {"Erro": "ID Item inexistente"}