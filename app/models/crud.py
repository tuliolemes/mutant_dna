from sqlalchemy.orm import Session
from typing import List
from . import models, schemas


def create_dna(db: Session, dna: schemas.Dna):
    db_dna = models.Dna(sequence=dna['sequence'], is_mutant=dna['is_mutant'])
    db.add(db_dna)
    db.commit()
    db.refresh(db_dna)
    return db_dna


def get_dna_by_sequence(db: Session, sequence: List[str]):
    #return db.query(models.Dna).filter(models.Dna.sequence in sequence).first()
    return db.query(models.Dna).filter(models.Dna.sequence == sequence).first()
    # return db.query(models.Dna).filter(models.Dna.sequence.in_(sequence)).first()


def count_human_dna(db: Session):
    return db.query(models.Dna).filter(models.Dna.is_mutant == False).count()


def count_mutant_dna(db: Session):
    return db.query(models.Dna).filter(models.Dna.is_mutant == True).count()
