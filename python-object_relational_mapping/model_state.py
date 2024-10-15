#!/usr/bin/python3
"""Write a python file that contains the class definition of a State and an
instance Base = declarative_base()"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
url = 'mysql+mysqldb://root:root@localhost:3306/states'
engine = create_engine(url)


class State(Base):
    """State Class inherits from Base"""
    __tablename__ = 'state'
    id = Column(Integer, primary_key=True, auto_generate=True, nullable=False,
                unique=True)
    name = Column(String(128))


Base.metadata.create_all(engine)

# if __name__ == "__main__":
#     pass
