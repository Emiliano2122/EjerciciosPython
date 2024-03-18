lista = [1, 2, 5, 7, 8, 10, 13, 14, 15, 17, 20]

valores_faltantes = []

for numero in range(1, 21):
    if numero not in lista:
        valores_faltantes.append(numero)

print("Valores faltantes en la lista:")
print(valores_faltantes)