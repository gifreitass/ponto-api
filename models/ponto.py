import datetime

from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from config import Base

class Ponto(Base):
    __tablename__ = 'pontos'

    id: Mapped[int] = mapped_column(primary_key=True)
    funcionario_nome: Mapped[str] = mapped_column(String(100))
    tipo: Mapped[str] = mapped_column(String(30))
    data_hora: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )