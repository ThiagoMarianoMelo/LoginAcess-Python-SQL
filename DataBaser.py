#importacao da biblioteca de ligacao entre python e o sql
import sqlite3

#inicializacao do BDD
conn = sqlite3.connect("UserData.db")

#criacao do cursor ligado ao dbb
cursor = conn.cursor()

#comando de criacao de table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    NAME TEXT NOT NULL,
    USER TEXT NOT NULL,
    PASSWORD TEXT NOT NULL  
);
""")

cursor.execute("""
DELETE FROM Users
WHERE ID = '1'
""")


print("conexao ok")
