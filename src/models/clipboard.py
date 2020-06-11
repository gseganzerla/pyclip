from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from src.models.sql import Sql


Base = declarative_base()


class Clipboard(Base):
    __tablename__ = "clipboards"

    id = Column(Integer, primary_key=True)
    clipboard = Column(String)
