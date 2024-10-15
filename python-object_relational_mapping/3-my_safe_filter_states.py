#!/usr/bin/python3
"""write a script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument. But this time, write
one that is safe from MySQL injections!"""
import MySQLdb
import sys

if __name__ == "__main__":
    """lists all states in an injection-safe method for user-input state."""
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    target = sys.argv[4]
    cur.execute("SELECT id, name \
                FROM states \
                WHERE BINARY name = %s \
                ORDER BY id ASC", (target,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
