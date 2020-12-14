i!/usr/bin/python3
"""list all states with its names start with N (Uppercase N)"""

if __name__ = '__main__':
	import MySQLdb
	import sys

	db = MySLQdb.connect(host='localhost', port=3306, user=sys.argv[1], passwd=sys.argsv[2], db=sys.argsv[3])

	cur = db.cursor()
	cur = execute("""SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER by states.id ASC;""")
	rows = cur.fetchall()
	for row in rows:
		print(row)
 
