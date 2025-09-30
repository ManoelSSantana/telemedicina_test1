from sqlalchemy import Column, String
from .database import Base

class User(Base):
    __tablename__ = "users"

    cpf = Column(String, primary_key=True, index=True)
    hashed_password = Column(String)
    role = Column(String)  # "paciente", "medico", "enfermeira"
