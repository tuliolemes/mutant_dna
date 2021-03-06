from sqlalchemy import Column, String, Boolean

from .database import Base


class Dna(Base):
    __tablename__ = "dna"

    sequence = Column(String, primary_key=True, index=True)
    is_mutant = Column(Boolean)
