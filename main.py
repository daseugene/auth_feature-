from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    ...


@app.get("/")
def read_root():
    return {"text"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return{"item_id": item_id, "q": q}


@app.post("/login/")
def sign_in(login: str, password: str):
    return()