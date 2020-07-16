import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="putain",
    database="products"
    )
cursor = mydb.cursor()
#cursor.execute("CREATE DATABASE products")
#cursor.execute("SHOW DATABASES")

#for db in cursor:
    #print(db)

#cursor.execute("CREATE TABLE products(name VARCHAR(255), category VARCHAR(255))")
cursor.execute("SHOW TABLES")
for tb in cursor:
    print(tb)
sqlFormula = "INSERT INTO products (name, category) VALUES (%s, %s)"
items = [   ("Simba", "Chips"),
            ("Lays", "Chips"),
            ("Coke","Cooldrink"),
            ("Fanta","Cooldrink"),
            ("Cadbury","Chocolates"),
            ("Tex","Chocolates"),
            ("Pepper Steak","Pies"),
            ("Chicken","Pies"),
            ("Pear","Fruit"),
            ("Apple","Fruit"),
            ("Orange","Fruit"),
            ("Vanilla","Cupcakes"),
            ("Chocolate","Cupcakes"),
            ("Spinach","Veggies"),
            ("Cabbage","Veggies"),]

cursor.executemany(sqlFormula, items)
mydb.commit
