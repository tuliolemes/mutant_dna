from fastapi import APIRouter, HTTPException, Depends
from app.endpoints.utils import parse_list, check_horizontal_genes, check_vertical_genes, check_diagonal_genes, \
    check_reversed_diagonal_genes
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


@router.post("/mutant")  # , response_model=schemas.Dna, response_model_exclude=["sequence"]
def create_dna(dna=Depends(parse_list), db: Session = Depends(get_db)):
    sequence_as_string = '[' + ','.join(str(e) for e in dna) + ']'
    db_dna = crud.get_dna_by_sequence(db, sequence=sequence_as_string)

    if db_dna:
        if getattr(db_dna, 'is_mutant'):
            return True
        else:
            raise HTTPException(status_code=403, detail="You are not a mutant and will be destroyed")
    else:
        is_mutant = check_dna(dna)
        dna_filled = {'sequence': sequence_as_string, 'is_mutant': is_mutant}
        crud.create_dna(db=db, dna=dna_filled)
        if is_mutant:
            return True
        else:
            raise HTTPException(status_code=403, detail="You are not a mutant and will be destroyed")


def check_dna(dna=Depends(parse_list)):
    mutant_gene = 0

    mutant_gene += check_horizontal_genes(dna)
    mutant_gene += check_vertical_genes(dna)
    mutant_gene += check_diagonal_genes(dna)
    mutant_gene += check_reversed_diagonal_genes(dna)

    if mutant_gene > 1:
        return True
    else:
        return False
