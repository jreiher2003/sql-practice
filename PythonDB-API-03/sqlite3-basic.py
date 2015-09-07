import sqlite3

conn = sqlite3.connect("example.db")

cursor = conn.cursor()

# create table
cursor.execute('''CREATE TABLE stocks
	(data text, trans text, sybol text, qty real, price real)''')

# insert a row of data
cursor.execute("INSERT INTO stocks VALUES ('2006-01=06', 'BUY','RHAT',100,35.14)")

# save (commit) the changes
conn.commit()

cursor.execute( "select * from stocks")

results = cursor.fetchall()

print results

conn.close()

