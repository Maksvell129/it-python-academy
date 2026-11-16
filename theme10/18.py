# Содержимое:
# name,price,category
# Laptop,1200,Electronics
# Phone,800,Electronics
# Book,25,Books
# Table,300,Furniture
#
# Напишите программу, которая:
# читает CSV;
# выводит названия всех товаров;
# находит товары дороже 500;
# считает их количество;
# выводит самый дорогой товар.
import csv

products = []

with open("products.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        products.append(row)


print(products)
print(", ".join([product["name"] for product in products]))
print(", ".join([product["name"] for product in products if int(product["price"]) > 500]))
print(len(products))
print(max(products, key=lambda product: int(product["price"])))
