import json
new_product = {
    "name": "Wireless Mouse",
    "price": 25.99,
    "quantity": 100,
    "brand": "Logitech",
    "category": "Electronics",
    "entry_date": "2025-05-01",
}

with open('archivosJSON/products.json', 'r') as file:
    products = json.load(file)


products.append(new_product)

with open('archivosJSON/products.json', 'w') as file:
    json.dump(products, file, indent=4)
