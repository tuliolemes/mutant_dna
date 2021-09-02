from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models import crud, models, schemas
from app.models.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/stats")
def read_dna(db: Session = Depends(get_db)):
    count_mutant_dna = crud.count_mutant_dna(db)
    count_human_dna = crud.count_human_dna(db)
    ratio = count_mutant_dna/(count_human_dna+count_mutant_dna)
    return {"count_mutant_dna": count_mutant_dna, "count_human_dna": count_human_dna, "ratio": round(ratio, 2)}
