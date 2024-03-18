contador = 0
numero = -15
lista = []
print(f"Empezar a cargar {lista} de numeros negativos")
for numero in range(-15, -1):
    lista.append(numero)
    contador += 1
    if numero % 2 == 0:
        print(f"{numero} es un número par.")