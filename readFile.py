#leer un archivo
with open('cuento.txt', 'r') as file:
    for line in file:
        print(line.strip())

#leer todas las lineas de una lista
with open('cuento.txt', 'r') as file:
    line = file.readlines()
    print(len(line))

#añadir texto
with open('cuento.txt', 'a') as file:
    file.write('\n\nBy: ChatGPT')

#sobreescribir texto
with open('cuento.txt', 'w') as file:
    file.write('\n\nBy: ChatGPT')

