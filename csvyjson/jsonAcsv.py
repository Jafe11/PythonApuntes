import json
import csv

# Abrir el archivo JSON
with open('csvyjson/datos.json', encoding='utf-8') as archivo_json:
    datos = json.load(archivo_json)

# Crear archivo CSV y escribir los datos
with open('csvyjson/datos_convertido.csv', 'w', newline='', encoding='utf-8') as archivo_csv:
    campos = datos[0].keys()  # Usa las claves del primer diccionario como encabezados
    escritor = csv.DictWriter(archivo_csv, fieldnames=campos)

    escritor.writeheader()
    escritor.writerows(datos)
