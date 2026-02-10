from fastapi import FastAPI 
app = FastAPI()

@app.get("user/{user_id}")
async def read_user():
      return {"user_id": "user_id"}


@app.get("/item/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
 
