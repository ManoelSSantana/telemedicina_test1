from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models

router = APIRouter()

@router.get("/professionals")
async def get_professionals(db: Session = Depends(get_db)):
    return {"message": "Professionals endpoint"}
