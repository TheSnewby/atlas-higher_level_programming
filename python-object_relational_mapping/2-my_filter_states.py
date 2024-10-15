#!/usr/bin/python3
"""a script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument."""
import MySQLdb
import sys
import re


if __name__ == "__main__":
    """lists all states with a name matching user-input."""
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    target = sys.argv[4]
    cur.execute("SELECT id, name FROM states WHERE name = {} \
                ORDER BY id ASC".format(target))
    # above line can also be have:  WHERE name LIKE 'N%'
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()