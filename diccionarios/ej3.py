frutas = {"manzana": 2.99, "pera": 3.50, "plátano": 4.00}

while True:
    while True:
        fruta = input("Dime la fruta: ")
        if fruta in frutas:
            break
        print("Esa fruta no existe")
    cantidad = float(input("Dime la cantidad: "))
    print(f"El precio total es de {cantidad * frutas.get(fruta)}")
    otra = input("¿Quieres hacer otra consulta? (Y)")
    if otra.upper() != "Y":
        break
