#!/usr/bin/python3
"""Module that contains class definition of a State and a Base instance"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Defines Class Base"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    engine = create_engine('mysql://username:password@localhost:3306/database_name')

    Base.metadata.create_all(engine)
