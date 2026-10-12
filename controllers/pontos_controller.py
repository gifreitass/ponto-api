from models.ponto import Ponto
from fastapi import APIRouter

router = APIRouter()

banco_de_dados = []

@router.post("/")
def add_ponto(ponto: Ponto):
    banco_de_dados.append(ponto)
    return ponto

@router.get("/")
def list_pontos():
    return banco_de_dados