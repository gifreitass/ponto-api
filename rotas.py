from fastapi import APIRouter
from controllers import pontos_controller as pontos

router = APIRouter()

router.include_router(pontos.router, prefix="/pontos")