import json

#lectura del archivo
with open('archivosJSON/products.json', 'r') as file:
    products = json.load(file)

for product in products:
    #print(product)
    print(f"producto: {product["name"]}, precio: {product["price"]}")
