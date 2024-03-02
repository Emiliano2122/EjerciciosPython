ciudades = ["Alemania", "Tokio", "Londres", "Paris", "Roma", "Moscu", "España", "Sideny", "Berlin"]

try:
    ciudades.remove("Paris")
except ValueError:
    print("La ciudad ya no esta en la lista.")

print("Lista de ciudades actualizadas:")
print(ciudades)