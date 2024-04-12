from fastapi import FastAPI
from routes.datos import datos

app = FastAPI()

app.include_router(datos)