from fastapi import FastAPI
from pydantic import BaseModel
from utils import generate_description

app = FastAPI()

@app.get("/ok")
async def ok_endpoint():
    return {"message": "ok"}

@app.get("/hello")
async def hello_endpoint(name: str = 'World'):
    return {"message": f"Hello, {name}!"}

@app.post("/orders")
async def place_order(product: str, units: int):
    return {"message": f"Order for {units} unit of {product} placed successfully!"}

class Order(BaseModel):
    product: str
    units: str

@app.post("/orders_pydantic")
async def place_order(order: Order):
    return {"message": f"Order for {order.units} units of {order.product} placed successfully!"}

class Product(BaseModel):
    name: str
    notes: str

@app.post("/product_description")
async def generate_product_description(product: Product):
    description = generate_description(f"Product: {product.name}, Notes: {product.notes}")
    return {"product_description": description}
