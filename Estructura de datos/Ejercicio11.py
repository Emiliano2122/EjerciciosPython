ciudades = ["Alemania", "Tokio", "Londres", "Paris", "Roma", "Moscu", "España", "Sideny", "Berlin"]

try:
    indice_ciudad_inexistente = ciudades.index("Brasi")
    print("Indice de la ciudad inexistente:", indice_ciudad_inexistente)
except ValueError:
    print("La ciudad no est en la lista")