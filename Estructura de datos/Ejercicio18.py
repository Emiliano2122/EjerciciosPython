tupla_enteros = tuple(range(1, 21))

print(tupla_enteros)

numero_20_esta = 20 in tupla_enteros
numero_30_esta = 30 in tupla_enteros


if numero_20_esta:
    print("El numero 20 esta")
else:
    print("El numero 20 no esta")

if numero_30_esta:
    print("El numero 30 esta")
else:
    print("El numero 30 no esta")