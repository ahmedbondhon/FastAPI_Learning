from fastapi import FastAPI
from pydantic import BaseModel

class item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

app = FastAPI()

@app.put("/item/{item_id}")
async def update_item(item_id: int, item: item):
    return {"item_id": item_id, **item.model_dump()}