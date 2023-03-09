import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "**",
    database = "novo"
)

nome = "Dan"
endereco = "Brasil"

cursor = mydb.cursor()

cursor.execute("insert into cliente (name, endereco) values (%s, %s)", (nome, endereco))

mydb.commit()
