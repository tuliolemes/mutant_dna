from pydantic import BaseModel
from typing import List


# Base before creating. Ex: we don't know the id number
class DnaBase(BaseModel):
    sequence: str
    is_mutant: bool


# Attributes we can't recover from api return. Ex: password
class DnaCreate(DnaBase):
    pass


# Base after creating. Ex: returning from API, we already know the id number
class Dna(DnaBase):

    class Config:
        orm_mode = True
