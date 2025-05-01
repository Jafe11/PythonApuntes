import csv

#leer un archivo csv
with open('products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)

#mostrar informacion por columna
with open('products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"Product: {row['name']}, price: {row['price']}, quantity: {row['quantity']}")
