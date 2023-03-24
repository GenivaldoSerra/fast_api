from core.config import settings

from sqlalchemy import Column, Integer, String, DateTime

from datetime import datetime


class CursoModel(settings.DBBaseModel):
    __table_args__ = {"schema": "acad"}
    __tablename__ = "cursos"
    
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    titulo: str = Column(String(150), nullable=False, unique=True)
    aulas: int = Column(Integer)
    horas: int = Column(Integer)
    data_criacao: datetime = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at: datetime = Column(DateTime, default=datetime.now(), nullable=False)