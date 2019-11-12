from sqlalchemy import Column, Integer, TEXT, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Brand(Base):
    __tablename__ = 'Brand'

    id = Column(Integer, autoincrement=True, unique=True, primary_key=True)
    name = Column(TEXT)

