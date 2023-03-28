import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'abcd1234'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create db
cursorObject.execute("CREATE DATABASE elderco")

print("Database created...")