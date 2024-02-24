numero = 100

limite_superior = 300

while numero <= limite_superior:
    if numero % 12 != 0:
        numero += 1
        continue
    print(numero)
    numero += 1