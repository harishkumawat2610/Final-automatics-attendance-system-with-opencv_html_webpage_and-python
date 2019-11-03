import pymysql

mydb = pymysql.connect(
  host="localhost",
  user="root",
  password="",
database="My_college"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE students_record (s_no INT AUTO_INCREMENT PRIMARY KEY,id int(20), name VARCHAR(255),present text(20), date date,morning time,evening time)")
mycursor.execute("SHOW TABLES")
mycursor.execute("SHOW COLUMNS FROM students_record")
for table in mycursor:
	print(table)