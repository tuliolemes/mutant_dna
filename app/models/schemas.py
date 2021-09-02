from pydantic import BaseModel


class DnaBase(BaseModel):
    sequence: str
    is_mutant: bool


class DnaCreate(DnaBase):
    pass


class Dna(DnaBase):

    class Config:
        orm_mode = True
