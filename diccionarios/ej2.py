cadenaUsuario = input("Introduce una cadena:")

dictFinal = {}

for i in range(0, len(cadenaUsuario)):
    if cadenaUsuario[i] not in cadenaUsuario[0:i]:
        dictFinal.update({cadenaUsuario[i]:cadenaUsuario.count(cadenaUsuario[i])})

print(dictFinal)