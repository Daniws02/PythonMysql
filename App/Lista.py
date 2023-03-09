import mysql.connector

from Usuario import Usuario

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "**",
    database = "banco"
)

cursor = mydb.cursor()

#cursor.execute("create table usuario(id int auto_increment primary key, nome varchar(255), sabor varchar(255))")

Usuarios = []

Usuario.Ler(Usuarios)



for i in Usuarios:
    cursor.execute("insert into usuario(nome, sabor) values(%s, %s)",(i.Nome, i.Sabor))

mydb.commit()