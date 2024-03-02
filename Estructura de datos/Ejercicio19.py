ciudades = ["Alemania", "Tokio", "Londres", "Paris", "Roma", "Moscu", "España", "Sidny", "Berlin"]
print(ciudades)
print("Cual quieres eliminar:")
ciudad = input()
print(ciudad)

if ciudad not in ciudades:
    ciudades.append(ciudad)
    mensaje = "La ciudad ya no esta en la lista agragado."
else:
    mensaje = "La ciudad ya esta en la lista."

print(mensaje)
print(ciudades)
