from fastapi import FastAPI, APIRouter, Request

from controllers.index_controller import router as index_router
from controllers.provincias_controller import router as provincia_router
# Aplicacion
app = FastAPI()

# Rutas API
api_router = APIRouter()

app.include_router(index_router, tags=["Index"])
app.include_router(provincia_router, tags=[
                   "Provincias"], prefix="/provincias")
