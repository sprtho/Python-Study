import sqlite3

#  -*- coding: utf-8 -*-

db = sqlite3.connect("Book.db")
cursor = db.cursor()

datas = [(1, "python"), (2, "java"), (3, "spring")]
cursor.execute("create table Book (no, title)")
cursor.executemany("insert into Book  values (?, ?)", datas)
print ('Row count: ' + str(cursor.rowcount))


cursor.execute("select * from Book")
for row in cursor:
    print( row[1])

cursor.execute("update Book set title='Python3' where no=1");

cursor.execute("select * from Book")
print (cursor.fetchall())
cursor.execute("select * from Book where no=1")
row = cursor.fetchone()
print('No 1 is ' + row[1])
cursor.close()
db.commit()
db.close()