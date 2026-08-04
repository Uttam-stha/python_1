from pydantic import BaseModel

class Item(BaseModel):
    name:str
    price: float
    in_stock: bool

@app.post("/items/")
def create_item(item: Item):
    return {"item": item}