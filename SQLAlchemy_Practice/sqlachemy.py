from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,relationship
from sqlalchemy import ForeignKey,Text
from typing import List

engine = create_engine('postgresql://postgres:ke12@localhost:5432/Python-Postgres')

class Base(DeclarativeBase):
    pass


print("CREATING TABLES >>>> ")
Base.metadata.create_all(engine)

