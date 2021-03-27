import mysql.connector

db = mysql.connector.connect(
    host= "localhost",
    user="root",
    passwd="",
    database="toko_mainan"
)

cursor=db.cursor()

sql = """CREATE TABLE customers(
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name Varchar(255),
    address Varchar(255)
)
"""

cursor.execute(sql)

print("Table customers berhasil")