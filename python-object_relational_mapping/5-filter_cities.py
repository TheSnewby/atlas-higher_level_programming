#!/usr/bin/python3
"""Write a script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa"""
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
    cur.execute("SELECT cities.name \
                FROM cities \
                INNER JOIN states ON cities.state_id = states.id \
                WHERE states.name = %s \
                ORDER BY cities.id ASC", (target,))
    rows = cur.fetchall()
    city_count = 0
    for row in rows:
        if city_count == 0:
            print(row[0], end='')
            city_count += 1
        else:
            print(', {}'.format(row[0]), end='')
    print()
    cur.close()
    db.close()
