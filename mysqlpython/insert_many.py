import mysql.connector

db= mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database = "toko_mainan"
)

cursor=db.cursor()
sql = "INSERt INTO customers (name,address) VALUES (%s, %s)"
values=[
    ("Aji","Klaten"),
    ("Rio","Karanganyar"),
    ("Udin","Karanganyar"),
    ("Nanda","Sragen")
]

for val in values :
    cursor.execute(sql,val)
    db.commit()
print("{} data ditambahkan".format(len(values)))