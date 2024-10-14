#!/usr/bin/python3
import MySQLdb
import sys
"""Write a script that lists all states from the database hbtn_0e_0_usa:

Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
Your code should not be executed when imported"""
db = MySQLdb.connect(host="localhost",
                     user=sys.argv[1],
                     passwd=sys.argv[2],
                     db=sys.argv[3])
cur = db.cursor()
cur.execute("SELECT states.id FROM {} ORDER BY states.id ASC".format(db))
cur.close()
db.close()
