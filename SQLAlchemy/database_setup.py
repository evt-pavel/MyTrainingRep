from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationships
from sqlalchemy import create_engine

Base = declarative_base()
engine = create_engine('sqlite:///books.db')

class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True)
    title = Column(String(60), nullable=False)
    author = Column(String(30), nullable=False)
    genre = Column(String(30))

Base.metadata.create_all(engine)
