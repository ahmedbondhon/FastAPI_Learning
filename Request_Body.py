from fastapi import FastAPI
from pydantic import BaseModel

class item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

app = FastAPI()

@app.post("/items/")
async def read_item(item: item):
    return item
