#!/usr/bin/python3
"""Write a script that prints the State object with the name passed as
argument from the database hbtn_0e_6_usa"""
import MySQLdb
import sqlalchemy
import sys
from model_state import Base, State
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


if __name__ == "__main__":
    """main function"""
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_database = sys.argv[3]
    mysql_target = sys.argv[4]

    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(mysql_username,
                                                           mysql_password,
                                                           mysql_database)
    engine = create_engine(url)
    Base.metadata.create_all(engine)
    Sesh = sessionmaker(bind=engine)
    session = Sesh()
    state = session.query(State).filter(
            State.name == '{}'.format(mysql_target)).first()

    if state:
        print("{}".format(state.id))
    else:
        print("Not found")
    session.close()
