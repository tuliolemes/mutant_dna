from fastapi import APIRouter, HTTPException, Depends, Query
from endpoints.utils import parse_list, check_horizontal_genes, check_vertical_genes, check_diagonal_genes, \
    check_reversed_diagonal_genes
from sqlalchemy.orm import Session
from typing import List, Optional

from models import crud, models, schemas
from models.database import SessionLocal, engine

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


@router.get("/mutant")
def read_dna(dna=Depends(parse_list), db: Session = Depends(get_db)):
    sequence_as_string = '[' + ','.join(str(e) for e in dna) + ']'
    db_dna = crud.get_dna_by_sequence(db, sequence=sequence_as_string)
    if db_dna is None:
        raise HTTPException(status_code=404, detail="Dna not found")
    return True


@router.get("/stats")
def read_dna(db: Session = Depends(get_db)):
    count_mutant_dna = crud.count_mutant_dna(db)
    count_human_dna = crud.count_human_dna(db)
    ratio = count_mutant_dna/(count_human_dna+count_mutant_dna)
    return {"count_mutant_dna": count_mutant_dna, "count_human_dna": count_human_dna, "ratio": round(ratio,2)}


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
        # raise HTTPException(status_code=403, detail="You are not a mutant and will be destroyed!")

