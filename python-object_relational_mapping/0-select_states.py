#!/usr/bin/python3
"""Write a script that lists all states from the database hbtn_0e_0_usa."""
import MySQLdb
import sys


if __name__ == "__main__":
    """Lists all states from the database."""
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT states.id FROM {} ORDER BY states.id ASC".format(db))
    cur.close()
    db.close()
