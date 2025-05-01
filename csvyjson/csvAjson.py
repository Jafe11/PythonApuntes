import csv
import json

# Abrir archivo CSV
with open('csvyjson/pruebacsv.csv', newline='', encoding='utf-8') as archivo_csv:
    lector = csv.DictReader(archivo_csv)
    datos = list(lector)

# Guardar como archivo JSON
with open('csvyjson/datos.json', 'w', encoding='utf-8') as archivo_json:
    json.dump(datos, archivo_json, indent=4, ensure_ascii=False)
