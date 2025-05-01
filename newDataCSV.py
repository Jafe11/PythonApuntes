import csv 
new_product = {
    "name": "Wireless Mouse",
    "price": 25.99,
    "quantity": 100,
    "brand": "Logitech",
    "category": "Electronics",
    "entry_date": "2025-05-01",
}

with open('products.csv', mode='a', newline='') as file:
    file.write("\n")
    csv_writer = csv.DictWriter(file,  fieldnames=new_product.keys())
    csv_writer.writerow(new_product)