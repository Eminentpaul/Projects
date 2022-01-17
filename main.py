import sqlite3
import random

name = "Ogochukwu"
age = random.randint(1, 30)
address = "Ngenanwanta"

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

table = """CREATE TABLE IF NOT EXISTS register(
    Name text,
    Age integer,
    Address text)"""


query = "INSERT INTO register VALUES('"+ name +"', '"+ str(age) +"', '"+ address +"')"
done = cursor.execute(query)
if done:
    query2 = "SELECT * FROM register "
    cursor.execute(query2)
    row = cursor.fetchall()
    print(row)
else:
    print("Not Successful")