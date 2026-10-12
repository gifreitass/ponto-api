from typing import Annotated

from fastapi.params import Depends
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session

from models.ponto import Ponto
from fastapi import APIRouter

from config import get_db
from models.ponto import Ponto

router = APIRouter()

class PontoCreate(BaseModel):
    funcionario_nome: str
    tipo: str

@router.post("/")
def add_ponto(ponto: PontoCreate,
              db: Annotated[Session, Depends(get_db)]):
    novo_ponto = Ponto(
        funcionario_nome=ponto.funcionario_nome,
        tipo=ponto.tipo
    )

    db.add(novo_ponto)
    db.commit()
    db.refresh(novo_ponto)

@router.get("/")
def list_pontos(db: Annotated[Session, Depends(get_db)]):
    statement = select(Ponto)

    pontos = db.scalars(statement).all()

    return pontos