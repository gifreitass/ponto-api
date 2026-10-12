from fastapi import FastAPI
from rotas import router
from config import Base, engine
import models

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router, prefix="")