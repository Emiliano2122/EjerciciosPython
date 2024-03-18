contador = 0
numero = -15
lista = []
print(f"Empezar a cargar {lista} de numeros negativos")
for indice, numero in enumerate(range(-15, -1), start=1):
    lista.append(numero)
    contador += 1
    if numero % 2 == 0:
        print(f"{numero} es un número par.")
print("Lista de numeros negativos cargada:")
print(lista)