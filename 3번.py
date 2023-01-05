import sqlite3

def Create_Table():
	db = sqlite3.connect("Person.db")
	cursor = db.cursor()
	cursor.execute("create table person(id , Name , age)")
	cursor.close()
	db.close()

def insert_m():
	connector = sqlite3.connect("Person.db")
	sql = "insert into person values(1 , 'Dominica' , '14')"
	connector.execute(sql)
	sql = "insert into person values(2 , 'Ruri' , '13')"
	connector.execute(sql)
	sql = "insert into person values(3 , 'Ruo' , '9')"
	connector.execute(sql)
	connector.commit()
	connector.close()

def Select_M():
	connector = sqlite3.connect("Person.db")
	cursor = connector.cursor()
	cursor.execute("select * from person")
	result = cursor.fetchall()
	
	for row in result:
		print(row[1] + " 의 나이는 " + row[2] + " 입니다.")
	cursor.close()
	connector.close()

if __name__=="__main__":
	Create_Table()
	
if __name__=="__main__":
	insert_m()
	Select_M()