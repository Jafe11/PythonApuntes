import csv

file_path = 'products.csv'
update_file_path = 'products_updated.csv'

with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    #obterner los nombre de las columnnas
    fieldnames = csv_reader.fieldnames + ['total_value']

    with open(update_file_path, mode='w', newline='') as update_file:
        csv_writer = csv.DictWriter(update_file, fieldnames=fieldnames)
        csv_writer.writeheader() #infomracion encavezado 
        
        for row in csv_reader:
            row['total_value'] = float(row['price']) * int(row['quantity'])
            csv_writer.writerow(row)
