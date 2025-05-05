import random

tabla = []

for indice_fila in range(5):
    fila = []
    for indice_columna in range(5):
        fila.append(random.randint(1, 100))
    tabla.append(fila)

suma_columnas = []
print(tabla)

for fila in tabla:
    for index in range(5):
        if index == 0:
            suma_columnas.append(fila[index])
        else:
            suma_columnas[index] += fila[index]
    print(sum(fila))