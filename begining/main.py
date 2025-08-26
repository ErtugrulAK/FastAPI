from fastapi import FastAPI
import random
from pydantic import BaseModel
from typing import Optional , Union


class Product(BaseModel):
    name : str
    price : float
    stock : int
    category : Union[str , None] = None
    inStock : Optional[bool] = None
    

app = FastAPI()

@app.get("/")
def read_root():
    return {"output":"Hello World"}

@app.get("/{person}")
def quote(person: str):
    quotes={
        "Edison": "Genius is one percent inspiration and ninety-nine percent perspiration.",
        "Tesla": "If you want to find the secrets of the universe, think in terms of energy, frequency and vibration.",
        "Einstein": "Imagination is more important than knowledge.",
        "Newton": "If I have seen further it is by standing on the shoulders of Giants."
    }
    if person == "random":
        temp = random.choice(list(quotes.values()))
    else:
        temp = quotes.get(person)


    #return quotes.get(person)
    return {"output": temp}


@app.post("/product/")
def product(product : Product):
    product_dict = product.dict()
    product.stock = max (0 , product.stock)
    product_dict.update({"stock" : product.stock})
    product_dict.update({"inStock" : product.stock > 0})
    
    return {"output" : product_dict}
    