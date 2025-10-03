from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models

router = APIRouter()

@router.get("/patients")
async def get_patients(db: Session = Depends(get_db)):
    return {"message": "Patients endpoint"}
