import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root'
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE ite4_website")
print("Database created successfully")
