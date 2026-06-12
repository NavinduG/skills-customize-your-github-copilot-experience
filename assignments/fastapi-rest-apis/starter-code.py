from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Building REST APIs with FastAPI")


class ItemCreate(BaseModel):
    title: str
    completed: bool = False


class Item(ItemCreate):
    id: int


items: list[Item] = []
next_id = 1


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI REST API assignment"}


@app.get("/items")
def list_items():
    return items


@app.post("/items", response_model=Item)
def create_item(item: ItemCreate):
    global next_id
    new_item = Item(id=next_id, **item.model_dump())
    next_id += 1
    items.append(new_item)
    return new_item


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: ItemCreate):
    for index, item in enumerate(items):
        if item.id == item_id:
            replacement = Item(id=item_id, **updated_item.model_dump())
            items[index] = replacement
            return replacement
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item.id == item_id:
            items.pop(index)
            return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")