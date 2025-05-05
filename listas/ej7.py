def main():
    lista1 = []
    lista2 = []
    lista3 = []

    for i in range(5):
        lista1.append(int(input(f"Introduce el número {i + 1} para la lista 1: ")))
        lista2.append(int(input("Introduce un número " + str(i + 1) + " para la lista 2: ")))
        lista3.append(lista1[i] + lista2[i])

    print(lista1)
    print(lista2)
    print(lista3)


main()