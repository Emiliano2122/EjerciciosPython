numero = 100

limite_superior = 300

while numero <= limite_superior:
    if numero % 3 == 0 and numero % 6 == 0:
        print(f"El numero divisible por 3 y multiplo de 6 dentro del rango es: {numero} ")
    numero += 1