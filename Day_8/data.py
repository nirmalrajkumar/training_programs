import MySQLdb

db = MySQLdb.connect(host='localhost',user='root',passwd='ids123',db='mydb')

cur = db.cursor()

cur.execute('select * from info')
data = cur.fetchall()
for row in data:
	print row[0]
	print row[1]

