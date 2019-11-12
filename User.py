from sqlalchemy import Column, Integer, TEXT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, autoincrement=True, unique=True, primary_key=True)
    first_name = Column(TEXT)
    last_name = Column(TEXT)
    birthday_date = Column(TEXT)
