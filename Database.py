import pymysql

mydb = pymysql.connect(
  host="localhost",
  user="root",
  password="",
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE My_college")

mycursor.execute("SHOW DATABASES")
#print all databases
for db in mycursor:
	print(db)