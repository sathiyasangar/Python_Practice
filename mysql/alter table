import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="crudpython"
)


mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE customers ADD ID INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST")
