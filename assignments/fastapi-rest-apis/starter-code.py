from typing import Optional, List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float


# Simple in-memory store
items: List[Item] = [Item(id=1, name="Example", description="An example item", price=9.99)]


@app.get("/")
def read_root():
    return {"message": "FastAPI REST API — service is running"}


@app.get("/items", response_model=List[Item])
def list_items():
    return items


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for it in items:
        if it.id == item_id:
            return it
    raise HTTPException(status_code=404, detail="Item not found")


@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    # naive duplicate id check
    for it in items:
        if it.id == item.id:
            raise HTTPException(status_code=400, detail="ID already exists")
    items.append(item)
    return item


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated: Item):
    for idx, it in enumerate(items):
        if it.id == item_id:
            items[idx] = updated
            return updated
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for idx, it in enumerate(items):
        if it.id == item_id:
            items.pop(idx)
            return {"detail": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("starter-code:app", host="127.0.0.1", port=8000, reload=True)
