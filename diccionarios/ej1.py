numUsuario = int(input("Introduce un número:"))

dictResultado = {}

for num in range(1, numUsuario + 1):
    dictResultado.update({num: num*num})

print(dictResultado)