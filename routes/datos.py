from fastapi import APIRouter
from config.db import conn
from models.data import productos
from typing import List
from schema.product import Product

datos = APIRouter()

@datos.get("/productos", response_model=List[Product])
def get_productos():
    return conn.execute(productos.select()).fetchall()

@datos.post("/productos")
def create_product(datos: Product):
    new_product = {"nombre": datos.nombre, "descripcion": datos.descripcion, "cantidad": datos.cantidad, "precio": datos.precio}
    conn.execute(productos.insert().values(new_product))
    conn.commit()
    return "Producto Creado"

@datos.put("/productos/{codigo}")
def update_productos(datos: Product, codigo: int):
    conn.execute(productos.update().values(nombre=datos.nombre, descripcion=datos.descripcion, cantidad=datos.cantidad, precio=datos.precio).where(productos.c.codigo == codigo))
    conn.commit()
    return "Producto Actualizado"

@datos.delete("/productos/{codigo}")
def delete_productos(codigo: int):
    conn.execute(productos.delete().where(productos.c.codigo == codigo))
    conn.commit()
    return "Producto Eliminado"