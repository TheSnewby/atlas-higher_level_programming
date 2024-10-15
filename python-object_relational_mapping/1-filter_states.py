#!/usr/bin/python3
"""Write a script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa"""
import MySQLdb
import sys
import re


if __name__ == "__main__":
    """lists all states with a name starting with N (upper N)."""
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        if re.search('d N*', row):
            print(row)
    cur.close()
    db.close()
