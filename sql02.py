import sqlite3
con = sqlite3.connect("Book.db")
cur = con.cursor()

#  -*- coding: utf-8 -*-
def MyFunc(str1,str2):
             s1 = str1.upper()
             s2 = str2.upper()
             return (s1 > s2) - (s1 < s2)
         
con.create_collation('myordering', MyFunc)
cur.execute("SELECT title FROM  Book ORDER BY  title COLLATE myordering")
for r in cur:
    print(r[0])
        
for l in con.iterdump():
    print(l)
    
with open('dump.sql','w') as f:
    for l in con.iterdump():
        f.write('{0}\n'.format(l))