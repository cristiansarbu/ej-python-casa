import random

lista = []

for i in range(0, 10):
    lista.append(random.randrange(1, 10))

for num in lista:
    print("Num: " + str(num) + " Cuadrado: " + str(num*num) + " Cubo: " + str(num*num*num))