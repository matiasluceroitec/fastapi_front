import requests
from fastapi import APIRouter, Response, Request
from starlette import status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from schemas.provincias_schemas import ProvinciaSchema


templates = Jinja2Templates(directory="templates")

router = APIRouter()


@router.get("", name="Provincias", response_class=HTMLResponse, response_model=ProvinciaSchema)
async def get(request: Request):
    headers = {'Content-Type': 'application/json ; charset=utf-8'}
    response = requests.get(
        "http://localhost:8000/provincias", headers=headers)

    return templates.TemplateResponse("provincias.html", {"request": request, "provincias": response.json()})
