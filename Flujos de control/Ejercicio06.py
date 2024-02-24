numero = 7

if isinstance(numero, int) and numero > 0:
    factorial = 1
    while numero > 1:
        factorial *= numero
        numero -= 1
    print(f"El factorial del nuemro es: {factorial}")
else:
    print("La variable debe contener un numero entero mayor a 0.")
print(type(numero))