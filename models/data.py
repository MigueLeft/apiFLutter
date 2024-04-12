from sqlalchemy import Table, Column, Integer, String, Numeric
from config.db import meta, con

productos = Table("productos", meta, 
             Column("codigo", Integer, primary_key=True, autoincrement=True), 
             Column("nombre", String(255)), 
             Column("descripcion", String(255)), 
             Column("cantidad", Integer), 
             Column("precio", Numeric))

meta.create_all(con)