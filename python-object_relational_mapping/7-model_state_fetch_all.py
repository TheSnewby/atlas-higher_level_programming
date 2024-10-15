#!/usr/bin/python3
"""
Write a script that lists all State objects from the database hbtn_0e_6_usa
"""
import MySQLdb
import sqlalchemy
import sys
from model_state import Base, State
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
mysql_database = sys.argv[3]

url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(mysql_username,
                                                       mysql_password,
                                                       mysql_database)
engine = create_engine(url)
connection = engine.connect()
query_result = connection.execute("SELECT * FROM states")
rows = query_result.fetchall()
for row in rows:
    print(row)

if __name__ == "__main__":
    """main function"""