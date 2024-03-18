cadena = 'Hola Mundo. Esto es una practico del lenguaje de programacion Python'

posiciones = []

for i in range(len(cadena)):
    if cadena[i] == "n":
        posiciones.append(i)

print("La letra 'n' aparece en las siguientes posiciones:")
print(posiciones)