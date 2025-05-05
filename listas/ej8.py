nombres = []
edades = []

while True:
    nombre = input("Introduce el nombre: ")
    if nombre == "*":
        break
    edad = int(input(f"Introduce la edad de {nombre}: "))
    nombres.append(nombre)
    edades.append(edad)

for i in range(len(edades)):
    if edades[i] >= 18:
        print(f"{nombres[i]} ({edades[i]}) es mayor de edad.")

for edad, nombre in zip(edades, nombres):
    if edad >= 18:
        print(f"{nombre} tiene {edad}")

print(max(edades))
print(max(nombres))

