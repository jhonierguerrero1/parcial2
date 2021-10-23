import mysql.connector

DB = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='mysql',
    port=3306
)

def getAllUsers():
    cursor = DB.cursor(dictionary=True)

    cursor.execute('show databases;')

    return cursor.fetchall()

def crearUsuario(nombre):
    cursor = DB.cursor(dictionary=True)
    cursor.execute("create database %s",(nombre))

    DB.commit()
    cursor.close()