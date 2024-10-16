#!/usr/bin/python3
"""Write a Python file similar to model_state.py named model_city.py
that contains the class definition of a City."""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State


Base = declarative_base()
# url = 'mysql+mysqldb://root:root@localhost:3306/states'
# engine = create_engine(url)


class City(Base):
    """
    City Class inherits from Base
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False,
                unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
