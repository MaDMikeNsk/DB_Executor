from sqlalchemy import Column, Integer, TEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class AutoUser(Base):
    __tablename__ = 'AutoUser'
    id = Column(Integer, autoincrement=True, unique=True, primary_key=True)
    auto_id = Column(Integer)
    user_id = Column(Integer)