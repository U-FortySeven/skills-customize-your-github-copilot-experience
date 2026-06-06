import os
import sqlite3
from typing import Optional, List

from fastapi import FastAPI, HTTPException, Header, Depends
from pydantic import BaseModel

DATABASE_PATH = os.path.join(os.path.dirname(__file__), "items.db")
API_KEY = "secret-api-key"

app = FastAPI()


class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float


def get_db_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


def require_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/")
def read_root():
    return {"message": "Secure FastAPI REST API running"}


@app.get("/items", response_model=List[Item])
def list_items():
    conn = get_db_connection()
    rows = conn.execute("SELECT id, name, description, price FROM items").fetchall()
    conn.close()
    return [Item(**dict(row)) for row in rows]


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    conn = get_db_connection()
    row = conn.execute(
        "SELECT id, name, description, price FROM items WHERE id = ?", (item_id,)
    ).fetchone()
    conn.close()
    if row is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return Item(**dict(row))


@app.post("/items", response_model=Item, status_code=201, dependencies=[Depends(require_api_key)])
def create_item(item: Item):
    conn = get_db_connection()
    cursor = conn.execute(
        "INSERT INTO items (name, description, price) VALUES (?, ?, ?)",
        (item.name, item.description, item.price),
    )
    conn.commit()
    item_id = cursor.lastrowid
    conn.close()
    return Item(id=item_id, **item.dict(exclude={"id"}))


@app.put("/items/{item_id}", response_model=Item, dependencies=[Depends(require_api_key)])
def update_item(item_id: int, item: Item):
    conn = get_db_connection()
    existing = conn.execute(
        "SELECT id FROM items WHERE id = ?", (item_id,)
    ).fetchone()
    if existing is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Item not found")
    conn.execute(
        "UPDATE items SET name = ?, description = ?, price = ? WHERE id = ?",
        (item.name, item.description, item.price, item_id),
    )
    conn.commit()
    conn.close()
    return Item(id=item_id, **item.dict(exclude={"id"}))


@app.delete("/items/{item_id}", dependencies=[Depends(require_api_key)])
def delete_item(item_id: int):
    conn = get_db_connection()
    cursor = conn.execute("DELETE FROM items WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"detail": "Item deleted"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("starter-code:app", host="127.0.0.1", port=8000, reload=True)
