import mysql.connector
import numpy as np
import matplotlib as plt
import pandas as pd
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="putain",
    database="products"
    )
mycursor = mydb.cursor()
#cursor.execute("CREATE DATABASE products")
mycursor.execute("SHOW DATABASES")

for db in mycursor:
    print(db)

#cursor.execute("CREATE TABLE products(name VARCHAR(255), category VARCHAR(255))")
mycursor.execute("SHOW TABLES")
for tb in mycursor:
    print(tb)

mycursor.execute("DELETE FROM products")
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

mycursor.executemany(sqlFormula, items)
mydb.commit()

mycursor.execute("SELECT * FROM products")
records = mycursor.fetchall()
print("The total number of products is:" , mycursor.rowcount)
nameList =[]
catList = []

for row in records:
    print("Name: " + row[0] + "Type:" + row[1])
    nameList.append(row[0])
    catList.append(row[1])
lenList = len(catList)
for i in range(lenList) :
    print(nameList[i] + '     ' + catList[i])

data = {"Name" : nameList,
        "Category" : catList
        }
df = pd.DataFrame( data, columns = ["Name" , "Category"])

print(df)
pd.value_counts(df["Category"]).plot.bar()
