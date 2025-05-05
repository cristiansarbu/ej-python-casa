import random

lista = []
for i in range(10):
    lista.append(random.randint(1, 100))

print(lista)
lista.sort(reverse=True)
print(lista)