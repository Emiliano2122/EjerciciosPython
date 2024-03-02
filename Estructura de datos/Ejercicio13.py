ciudades = ["Alemania", "Tokio", "Londres", "Paris", "Roma", "Moscu", "España", "Sideny", "Berlin"]
print(ciudades)
print("Cual quieres eliminar:")
ciudad = input()
print(ciudad)

try:
    ciudades.remove(ciudad)
    print("La ciudad se elimino")
except ValueError:
    print("La ciudad ya no esta en la lista.")

try:
    ciudades.remove(ciudad)
except ValueError:
    print("La ciudad ya no esta en la lista.")

print("Lista de ciudades actualizadas:")
print(ciudades)
