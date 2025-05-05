num_alumnos = int(input("Introduce número de alumnos: "))
diccionario = {}

for i in range(num_alumnos):
    nombre = input("Dime nombre del alumno: ")
    notas = []
    while True:
        nota = int(input("Dime la nota: "))
        if nota < 0:
            break
        notas.append(nota)
    diccionario[nombre] = notas

print(diccionario)

for nombre, notas in diccionario.items():
    print(f"La media de {nombre} es {sum(notas) / len(notas):.2f}")

