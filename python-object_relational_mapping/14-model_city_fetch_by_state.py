#!/usr/bin/python3
""" write a script 14-model_city_fetch_by_state.py that prints
all City objects from the database hbtn_0e_14_usa."""
import MySQLdb
import sqlalchemy
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


if __name__ == "__main__":
    """main function"""
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_database = sys.argv[3]

    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(mysql_username,
                                                           mysql_password,
                                                           mysql_database)
    engine = create_engine(url)
    Base.metadata.create_all(engine)
    Sesh = sessionmaker(bind=engine)
    session = Sesh()
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print('{}: ({}) ({})'.format(
            session.query(State).filter_by(id=city.state_id).first().name,
            city.id,
            city.name
        ))

    session.close()
