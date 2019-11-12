from sqlalchemy import Column, Integer, TEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Auto(Base):
    __tablename__ = 'Auto'

    id = Column(Integer, autoincrement=True, unique=True, primary_key=True)
    name = Column(TEXT)
    year = Column(Integer)
