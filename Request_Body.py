from fastapi import FastAPI
from pydantic import BaseModel

class item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

app = FastAPI()

@app.post("/items/")
async def read_item(item: item):
    item_dict = item.model_dump()
    if item.text is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"Price with tax:" price_with_tax})
    return item_dict