from sqlalchemy import Column, Integer, TEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class AutoBrand(Base):
    __tablename__ = 'AutoBrand'
    id = Column(Integer, autoincrement=True, unique=True, primary_key=True)
    auto_id = Column(Integer)
    brand_id = Column(Integer)