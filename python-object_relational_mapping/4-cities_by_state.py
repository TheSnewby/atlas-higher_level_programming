#!/usr/bin/python3
"""Write a script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys

#!/usr/bin/python3
"""write a script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument. But this time, write
one that is safe from MySQL injections!"""
import MySQLdb
import sys

if __name__ == "__main__":
    """lists all cities from a database."""
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, state.name \
                FROM cities, states \
                ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
