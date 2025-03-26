from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mensagem": "Bem-vindo à minha API!"}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "nome": f"Item {item_id}"}
