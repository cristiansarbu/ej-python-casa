cadenaUsuario = input("Introduce tu nombre y apellidos:")

cadenaFinal = ""
for palabra in cadenaUsuario.split(" "):
    cadenaFinal = cadenaFinal + palabra.capitalize() + " "

print(cadenaFinal)