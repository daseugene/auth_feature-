from typing import Union, Annotated
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from setting import oauth2_scheme, pwd_context


app = FastAPI()



@app.get("/")
def read_root():
    return {"text"}

@app.get("/items/{item_id}")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)], item_id: int, q: Union[str, None] = None):
    return{"access": token}
    return{"item_id": item_id, "q": q}

@app.post("/login/")
def sign_in(login: str, password: str):
    return()

