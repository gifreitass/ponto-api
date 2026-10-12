import datetime

from pydantic import BaseModel

class Ponto(BaseModel):
    id: int
    date: datetime.date
    time: datetime.time
    username: str